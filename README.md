# Smart-Canteen-Ordering-and-Billing-System

## Project Overview

The **Smart Canteen Ordering and Billing System** is a command-line Python application designed to computerize basic college canteen operations. It allows customers to view and search the food menu, place and modify orders, calculate bills, select a payment method, and save completed bills.

The project also includes an administrator section for viewing inventory, restocking items, updating prices, adding food items, and removing food items.

## Features

### Customer
- View food menu
- Search food by name or category
- Add food items to an order
- Check stock availability
- View current order
- Remove items or clear the order
- Automatic subtotal calculation
- 5% GST calculation
- 10% discount when subtotal is ₹500 or above
- Cash, UPI, and Card payment selection
- Automatic bill generation
- Bill storage in `canteen_bills.txt`

### Administrator
- Admin login
- View inventory
- Identify low-stock items
- Restock food items
- Update prices
- Add new food items
- Remove food items

## Technologies Used

- Python 3
- Python dictionaries
- Functions
- `if`, `elif`, `else`
- `for` and `while` loops
- Exception handling
- File handling
- `datetime`

No third-party Python packages are required.

## Requirements

- Python 3.8 or later
- Command Prompt / Terminal

## Installation and Setup

### 1. Install Python

Install Python 3 from the official Python website if it is not already installed.

### 2. Download or clone the repository

Using Git:

```bash
git clone https://github.com/YOUR-USERNAME/Smart-Canteen-Ordering-and-Billing-System.git
cd Smart-Canteen-Ordering-and-Billing-System
```

Alternatively, download the repository as a ZIP file from GitHub and extract it.

### 3. Check Python

Run:

```bash
python --version
```

If your system uses `python3`, run:

```bash
python3 --version
```

### 4. Run the project

Windows:

```bash
python main.py
```

Linux/macOS:

```bash
python3 main.py
```

The application runs entirely in the terminal. No GUI setup or third-party package installation is required.

## How to Use

### Customer

1. Select `1. Customer`.
2. Enter the customer name.
3. Select an operation from the customer menu.
4. View or search the menu.
5. Add the required food items and quantities.
6. View or modify the order.
7. Select checkout.
8. Select Cash, UPI, or Card.
9. The final bill is displayed and saved automatically.

### Administrator

Select `2. Admin`.

Educational login credentials:

```text
Username: admin
Password: 1234
```

The administrator can then manage inventory and food items.

## Billing Formula

```text
Subtotal = Sum(Price × Quantity)
GST = Subtotal × 5%

If Subtotal >= ₹500:
    Discount = Subtotal × 10%
Else:
    Discount = ₹0

Final Amount = Subtotal + GST - Discount
```

## Generated Files

After a successful checkout, the program creates/appends to:

```text
canteen_bills.txt
```

This file contains order ID, customer name, date/time, payment method, ordered items, subtotal, GST, discount, and final amount.

`canteen_bills.txt` is generated automatically and does not need to exist before the first run.

## Project Structure

```text
Smart-Canteen-Ordering-and-Billing-System/
│
├── main.py
├── README.md
├── project_report.pdf
└── canteen_bills.txt        # generated after checkout
```

## Testing

The project was designed to test:
- Valid and invalid food item selection
- Quantity greater than available stock
- Valid quantities
- Orders below and above the discount threshold
- Cash, UPI, and Card selection
- Checkout and bill generation
- Inventory reduction after checkout
- Valid and invalid administrator login
- Bill storage in the text file

## Important Note

This is an educational command-line project. Payment selection is simulated and is not connected to a real payment gateway. Inventory is stored in memory during execution, while completed bills are stored in a text file.

## Author

**Divyanshi Patel**  
CSE Core  
VIT Bhopal University
