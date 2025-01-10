# Inventory Management System

## Overview

This Inventory Management System is built using Django to efficiently manage products, stock levels, suppliers, and sales. The system provides CRUD operations for products and suppliers, facilitates stock management, and enables tracking of sales orders. It ensures proper validation and seamless integration between frontend and backend components.

## Features

### Mandatory Features

1. Add Product:
    1. Add a new product to the inventory with validation for stock quantity, price, and product details.
    2. Prevent duplicate product records.

2. List Products:
    1. Retrieve and display a list of all products, including their name, description, price, stock quantity, and supplier details.

3. Add Supplier:
    1. Add a new supplier with validation for email and phone number format.
    2. Prevent duplicate supplier records.
  
4. List Suppliers:
    1. Retrieve and display a list of all suppliers with their name, email, phone, and address details.
  
5. Add Stock Movement:
    1. Record incoming stock ("In") or outgoing stock ("Out") and update stock levels accordingly.
    2. Validate stock levels to prevent negative values.
  
6. Create Sale Order:
    1. Allow users to create sale orders by selecting products, verifying sufficient stock, and calculating the total price.
    2. Update stock levels after each sale.
  
7. Cancel Sale Order:
    1. Cancel an existing sale order by setting its status to "Cancelled."
    2. Update stock levels to reflect the cancellation. 

8. Complete Sale Order:
    1. Mark a sale order as "Completed" and update stock levels accordingly.
  
9. List Sale Orders:
    1. Retrieve and display all sale orders, including product name, quantity, total price, sale date, status, and additional notes.
  
10. Stock Level Check:
    1. Implement a function to check and return the current stock level for each product.
   
### Additional Features

1. User Interface:
    1. User-friendly UI with seamless backend integration.
  
2. Filtering:
    1. Implement filtering options (e.g., by product category or order status).
  
3. Data Validation:
    1. Validate all inputs such as email formats, phone numbers, and stock levels.
  
## Tech Stack

1. Backend: Django
2. Frontend: HTML, CSS, JavaScript
3. Database: SupabaseDB

## Database Models

1. Product
    1. name: varchar
    2. description: text
    3. category: varchar
    4. price: float8
    5. stock_quantity: numeric
    6. supplier: varchar (foreign key to Supplier)
  
2. Supplier
    1. name: varchar
    2. email: varchar
    3. phone: numeric
    4. address: text

3. SaleOrder
    1. product: text (foreign key to Product)
    2. quantity: numeric
    3. total_price: float8
    4. sale_date: date
    5. status: varchar (Pending/Completed/Cancelled)

4. StockMovement
    1. product: text (foreign key to Product)
    2. quantity: numeric
    3. movement_type: varchar ("In" for incoming stock, "Out" for sales)
    4. movement_date: date
    5. notes: text
  
## Usage

1. Navigate to the UI to manage products, suppliers, stock movements, and sale orders.
2. Use the provided forms to add, list, and manage data.
3. Use filtering options to narrow down your data view.

## Image

![Inventory Management System](https://drive.google.com/uc?id=1Oex6kExoERVeKmgiQSHjEVQLcqWpJ_YD)
