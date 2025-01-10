from django.db import models
from django.core.validators import MinValueValidator, RegexValidator


class Supplier(models.Model):
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, validators=[
                             RegexValidator(r'^\d{10,15}$')])
    address = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    category = models.CharField(max_length=255)
    price = models.FloatField(validators=[MinValueValidator(0.01)])
    stock_quantity = models.PositiveIntegerField(default=0)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class StockMovement(models.Model):
    MOVEMENT_CHOICES = [
        ('In', 'Incoming'),
        ('Out', 'Outgoing'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    movement_type = models.CharField(max_length=3, choices=MOVEMENT_CHOICES)
    movement_date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.movement_type == 'In':
            self.product.stock_quantity += self.quantity
        elif self.movement_type == 'Out':
            if self.product.stock_quantity < self.quantity:
                raise ValueError("Insufficient stock for the operation.")
            self.product.stock_quantity -= self.quantity
        self.product.save()
        super().save(*args, **kwargs)


class SaleOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.FloatField()
    sale_date = models.DateField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Completed', 'Completed'),
                 ('Cancelled', 'Cancelled')],
    )
    notes = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:  # New sale order creation
            if self.quantity > self.product.stock_quantity:
                raise ValueError("Insufficient stock!")
            self.total_price = self.product.price * self.quantity
            self.product.stock_quantity -= self.quantity
            self.product.save()
        else:  # Update existing order
            original = SaleOrder.objects.get(pk=self.pk)
            # Only adjust stock for specific status changes
            if original.status == 'Pending' and self.status == 'Cancelled':
                self.product.stock_quantity += original.quantity
                self.product.save()

        super().save(*args, **kwargs)
