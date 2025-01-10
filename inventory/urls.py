from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-product/', views.add_product, name='add_product'),
    path('list-products/', views.list_products, name='list_products'),
    path('add-supplier/', views.add_supplier, name='add_supplier'),
    path('list-suppliers/', views.list_suppliers, name='list_suppliers'),
    path('add-stock-movement/', views.add_stock_movement,
         name='add_stock_movement'),
    path('create-sale-order/', views.create_sale_order, name='create_sale_order'),
    path('cancel-sale-order/<int:order_id>/',
         views.cancel_sale_order, name='cancel_sale_order'),
    path('complete-sale-order/<int:order_id>/',
         views.complete_sale_order, name='complete_sale_order'),
    path('sale-orders/', views.list_sale_orders, name='list_sale_orders'),
    path('stock-levels/', views.stock_level_check, name='stock_level_check'),
]
