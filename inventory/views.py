from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product, Supplier, StockMovement, SaleOrder
from django.db.models import F
from django.core.exceptions import ValidationError


def home(request):
    return render(request, 'base.html')


def add_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        category = request.POST['category']
        price = request.POST['price']
        stock_quantity = request.POST['stock_quantity']
        supplier_id = request.POST['supplier']

        if Product.objects.filter(name=name).exists():
            messages.error(request, "Product already exists!")
        else:
            supplier = Supplier.objects.get(id=supplier_id)
            Product.objects.create(
                name=name,
                description=description,
                category=category,
                price=price,
                stock_quantity=stock_quantity,
                supplier=supplier,
            )
            messages.success(request, "Product added successfully!")
            return redirect('list_products')

    suppliers = Supplier.objects.all()
    return render(request, 'add_product.html', {'suppliers': suppliers})


def list_products(request):
    products = Product.objects.select_related('supplier')
    return render(request, 'list_products.html', {'products': products})


def add_supplier(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']

        if Supplier.objects.filter(name=name).exists():
            messages.error(request, "Supplier already exists!")
        else:
            Supplier.objects.create(
                name=name, email=email, phone=phone, address=address)
            messages.success(request, "Supplier added successfully!")
            return redirect('list_suppliers')

    return render(request, 'add_supplier.html')


def list_suppliers(request):
    suppliers = Supplier.objects.all()
    return render(request, 'list_suppliers.html', {'suppliers': suppliers})


def add_stock_movement(request):
    if request.method == 'POST':
        product_id = request.POST['product']
        quantity = int(request.POST['quantity'])
        movement_type = request.POST['movement_type']
        notes = request.POST['notes']

        try:
            product = Product.objects.get(id=product_id)
            StockMovement.objects.create(
                product=product,
                quantity=quantity,
                movement_type=movement_type,
                notes=notes,
            )
            messages.success(request, "Stock movement recorded successfully!")
            return redirect('list_products')
        except ValueError as e:
            messages.error(request, str(e))

    products = Product.objects.all()
    return render(request, 'add_stock_movement.html', {'products': products})


def create_sale_order(request):
    if request.method == 'POST':
        product_id = request.POST['product']
        quantity = int(request.POST['quantity'])
        product = Product.objects.get(id=product_id)

        if quantity > product.stock_quantity:
            return render(request, 'create_sale_order.html', {'error': 'Insufficient stock', 'products': Product.objects.all()})

        sale_order = SaleOrder(
            product=product, quantity=quantity, status='Pending')
        sale_order.save()
        return redirect('list_sale_orders')

    return render(request, 'create_sale_order.html', {'products': Product.objects.all()})


def cancel_sale_order(request, order_id):
    sale_order = SaleOrder.objects.get(id=order_id)
    if sale_order.status == 'Pending':
        sale_order.status = 'Cancelled'
        sale_order.save()
    return redirect('list_sale_orders')


def complete_sale_order(request, order_id):
    sale_order = SaleOrder.objects.get(id=order_id)
    if sale_order.status == 'Pending':
        sale_order.status = 'Completed'
        sale_order.save()
    return redirect('list_sale_orders')


def list_sale_orders(request):
    sale_orders = SaleOrder.objects.all()
    return render(request, 'list_sale_orders.html', {'sale_orders': sale_orders})


def stock_level_check(request):
    products = Product.objects.all()
    return render(request, 'stock_level_check.html', {'products': products})
