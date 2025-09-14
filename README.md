# Store Management System

This **Store Management System** is a console-based Python application designed to manage products, customers, and sales efficiently. It simulates the key functionalities of a real-world store, allowing users to add products, manage customers, process sales, and track revenue using CSV files for persistent storage.

## Features

**Product Management:** Easily add, update, and organize products using unique IDs, names, prices, and quantities. The system ensures accurate stock tracking and prevents negative quantities.

**Customer Management:**

- **Add Customers:** Register new customers with unique IDs, names, and phone numbers.
- **Customer Lookup:** Quickly access customer information for processing sales.

**Sales & Transactions:**

- **Sell Products:** Sell products to registered customers while ensuring enough stock is available.
- **Track Sales:** Each sale is recorded with details including customer ID, product ID, quantity, total price, and timestamp.
- **Revenue Tracking:** Total revenue is automatically calculated and displayed.

**Data Management:**

- **Persistent Storage:** All products, customers, and sales are stored in CSV files (`products.csv`, `customers.csv`, `sales.csv`).
- **Clear Data:** Option to reset all store data and CSV files.

## Technical Highlights

**Data Structures:** Uses Python dictionaries for fast access and management of products and customers. Lists store sales records for easy iteration and aggregation.

**Object-Oriented Programming (OOP):** Follows OOP principles, representing each entity (Product, Customer, Sale) as a class, making the system modular, maintainable, and extensible.

**User Interaction:** Features an interactive console menu, allowing users to navigate through functionalities like adding products, selling items, listing products and sales, and clearing data.

## Future Improvements

- Add support for product categories and filtering.
- Integrate a graphical user interface (GUI) for a more interactive experience.
