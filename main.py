from datetime import datetime

CANTEEN_NAME = "SMART CANTEEN"
GST_RATE = 0.05
DISCOUNT_RATE = 0.10
DISCOUNT_LIMIT = 500
LOW_STOCK_LIMIT = 5
BILL_FILE = "canteen_bills.txt"
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "1234"

menu = {
    1: {"name": "Veg Burger", "category": "Burger", "price": 60, "stock": 20},
    2: {"name": "Cheese Burger", "category": "Burger", "price": 80, "stock": 15},
    3: {"name": "Veg Pizza", "category": "Pizza", "price": 120, "stock": 12},
    4: {"name": "Paneer Pizza", "category": "Pizza", "price": 150, "stock": 10},
    5: {"name": "French Fries", "category": "Snacks", "price": 80, "stock": 25},
    6: {"name": "Veg Sandwich", "category": "Snacks", "price": 70, "stock": 18},
    7: {"name": "Samosa", "category": "Snacks", "price": 20, "stock": 40},
    8: {"name": "Masala Dosa", "category": "South Indian", "price": 90, "stock": 15},
    9: {"name": "Idli Sambar", "category": "South Indian", "price": 60, "stock": 20},
    10: {"name": "Veg Biryani", "category": "Main Course", "price": 110, "stock": 14},
    11: {"name": "Paneer Rice", "category": "Main Course", "price": 100, "stock": 12},
    12: {"name": "Cold Drink", "category": "Beverages", "price": 40, "stock": 30},
    13: {"name": "Tea", "category": "Beverages", "price": 20, "stock": 50},
    14: {"name": "Coffee", "category": "Beverages", "price": 30, "stock": 40},
    15: {"name": "Ice Cream", "category": "Dessert", "price": 50, "stock": 20},
    16: {"name": "Gulab Jamun", "category": "Dessert", "price": 45, "stock": 25},
}

order = {}
order_id = 1000


def line(char="=", size=68):
    print(char * size)


def title(text):
    line()
    print(text.center(68))
    line()


def pause():
    input("\nPress Enter to continue...")


def money(value):
    return f"₹{value:.2f}"


def get_next_order_id():
    global order_id
    order_id += 1
    return order_id


def calculate_subtotal():
    subtotal = 0
    for item_no, quantity in order.items():
        subtotal += menu[item_no]["price"] * quantity
    return subtotal


def calculate_bill_values():
    subtotal = calculate_subtotal()
    gst = subtotal * GST_RATE
    discount = subtotal * DISCOUNT_RATE if subtotal >= DISCOUNT_LIMIT else 0
    final_amount = subtotal + gst - discount
    return subtotal, gst, discount, final_amount


def display_menu():
    title("SMART CANTEEN FOOD MENU")
    print(f"{'No.':<5}{'Item':<24}{'Category':<18}{'Price':>10}{'Stock':>10}")
    line("-")
    for number, item in menu.items():
        print(
            f"{number:<5}{item['name']:<24}{item['category']:<18}"
            f"{money(item['price']):>10}{item['stock']:>10}"
        )
    line("-")


def display_categories():
    title("FOOD CATEGORIES")
    categories = []
    for item in menu.values():
        if item["category"] not in categories:
            categories.append(item["category"])
    for index, category in enumerate(categories, 1):
        print(f"{index}. {category}")


def search_food():
    title("SEARCH FOOD")
    keyword = input("Enter item name or category: ").strip().lower()
    found = False
    for number, item in menu.items():
        if keyword in item["name"].lower() or keyword in item["category"].lower():
            print(
                f"{number}. {item['name']} - {money(item['price'])} "
                f"- Stock: {item['stock']}"
            )
            found = True
    if not found:
        print("No matching food item found.")


def add_item():
    display_menu()
    try:
        item_no = int(input("Enter item number: "))
        if item_no not in menu:
            print("Invalid item number.")
            return
        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return
        current = order.get(item_no, 0)
        if current + quantity > menu[item_no]["stock"]:
            print("Not enough stock available.")
            return
        order[item_no] = current + quantity
        print(f"{quantity} x {menu[item_no]['name']} added to order.")
    except ValueError:
        print("Please enter valid numbers.")


def view_order():
    title("CURRENT ORDER")
    if not order:
        print("Your order is empty.")
        return
    print(f"{'No.':<5}{'Item':<25}{'Qty':<8}{'Amount':>12}")
    line("-")
    for item_no, quantity in order.items():
        item = menu[item_no]
        amount = item["price"] * quantity
        print(f"{item_no:<5}{item['name']:<25}{quantity:<8}{money(amount):>12}")
    line("-")
    print(f"Subtotal: {money(calculate_subtotal())}")


def remove_item():
    if not order:
        print("Your order is empty.")
        return
    view_order()
    try:
        item_no = int(input("Enter item number to remove: "))
        if item_no not in order:
            print("Item is not in your order.")
            return
        quantity = int(input("Enter quantity to remove: "))
        if quantity <= 0:
            print("Quantity must be positive.")
        elif quantity >= order[item_no]:
            del order[item_no]
            print("Item removed completely.")
        else:
            order[item_no] -= quantity
            print("Order quantity updated.")
    except ValueError:
        print("Please enter a valid number.")


def clear_order():
    if not order:
        print("Your order is already empty.")
        return
    confirm = input("Clear entire order? (y/n): ").lower()
    if confirm == "y":
        order.clear()
        print("Order cleared.")
    else:
        print("Order was not cleared.")


def generate_bill(customer_name, payment_method="Not Paid"):
    if not order:
        print("Cannot generate a bill for an empty order.")
        return
    subtotal, gst, discount, final_amount = calculate_bill_values()
    bill_no = get_next_order_id()
    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    title("FINAL BILL")
    print(f"Order ID : {bill_no}")
    print(f"Customer Name : {customer_name}")
    print(f"Date and Time : {now}")
    print(f"Payment Method : {payment_method}")
    line("-")
    print(f"{'Item':<25}{'Qty':<8}{'Rate':<12}{'Amount':>12}")
    line("-")
    for item_no, quantity in order.items():
        item = menu[item_no]
        amount = item["price"] * quantity
        print(
            f"{item['name']:<25}{quantity:<8}{money(item['price']):<12}"
            f"{money(amount):>12}"
        )
    line("-")
    print(f"Subtotal : {money(subtotal)}")
    print(f"GST (5%) : {money(gst)}")
    print(f"Discount : {money(discount)}")
    print(f"Final Amount : {money(final_amount)}")
    line()
    print("Thank you for ordering from Smart Canteen!")
    return bill_no, final_amount


def choose_payment():
    title("PAYMENT METHOD")
    print("1. Cash")
    print("2. UPI")
    print("3. Card")
    while True:
        choice = input("Choose payment method: ").strip()
        if choice == "1":
            return "Cash"
        if choice == "2":
            return "UPI"
        if choice == "3":
            return "Card"
        print("Invalid payment choice.")


def save_bill(customer_name, bill_no, payment_method):
    subtotal, gst, discount, final_amount = calculate_bill_values()
    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    with open(BILL_FILE, "a", encoding="utf-8") as file:
        file.write("\n" + "=" * 68 + "\n")
        file.write("SMART CANTEEN BILL\n")
        file.write("=" * 68 + "\n")
        file.write(f"Order ID: {bill_no}\n")
        file.write(f"Customer: {customer_name}\n")
        file.write(f"Date: {now}\n")
        file.write(f"Payment: {payment_method}\n")
        for item_no, quantity in order.items():
            item = menu[item_no]
            amount = item["price"] * quantity
            file.write(f"{item['name']} x {quantity} = ₹{amount:.2f}\n")
        file.write(f"Subtotal: ₹{subtotal:.2f}\n")
        file.write(f"GST: ₹{gst:.2f}\n")
        file.write(f"Discount: ₹{discount:.2f}\n")
        file.write(f"Final Amount: ₹{final_amount:.2f}\n")
    print(f"Bill saved to {BILL_FILE}.")


def checkout(customer_name):
    if not order:
        print("Your order is empty.")
        return
    payment = choose_payment()
    result = generate_bill(customer_name, payment)
    if result:
        bill_no, amount = result
        save_bill(customer_name, bill_no, payment)
        for item_no, quantity in order.items():
            menu[item_no]["stock"] -= quantity
        order.clear()
        print(f"Payment of {money(amount)} recorded successfully.")


def admin_login():
    title("ADMIN LOGIN")
    username = input("Username: ")
    password = input("Password: ")
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("Admin login successful.")
        return True
    print("Invalid admin credentials.")
    return False


def show_inventory():
    title("INVENTORY")
    print(f"{'No.':<5}{'Item':<25}{'Stock':>10}{'Status':>15}")
    line("-")
    for number, item in menu.items():
        status = "LOW STOCK" if item["stock"] <= LOW_STOCK_LIMIT else "Available"
        print(f"{number:<5}{item['name']:<25}{item['stock']:>10}{status:>15}")


def restock_item():
    show_inventory()
    try:
        item_no = int(input("Enter item number: "))
        if item_no not in menu:
            print("Invalid item.")
            return
        quantity = int(input("Enter quantity to add: "))
        if quantity <= 0:
            print("Quantity must be positive.")
            return
        menu[item_no]["stock"] += quantity
        print("Stock updated successfully.")
    except ValueError:
        print("Enter valid numbers.")


def update_price():
    display_menu()
    try:
        item_no = int(input("Enter item number: "))
        if item_no not in menu:
            print("Invalid item.")
            return
        price = float(input("Enter new price: "))
        if price <= 0:
            print("Price must be positive.")
            return
        menu[item_no]["price"] = price
        print("Price updated successfully.")
    except ValueError:
        print("Enter a valid price.")


def add_food_item():
    title("ADD FOOD ITEM")
    try:
        number = max(menu.keys()) + 1
        name = input("Food name: ").strip()
        category = input("Category: ").strip()
        price = float(input("Price: "))
        stock = int(input("Initial stock: "))
        if not name or not category or price <= 0 or stock < 0:
            print("Invalid food details.")
            return
        menu[number] = {
            "name": name,
            "category": category,
            "price": price,
            "stock": stock,
        }
        print(f"Food item added with number {number}.")
    except ValueError:
        print("Enter valid price and stock.")


def remove_food_item():
    display_menu()
    try:
        number = int(input("Enter item number to delete: "))
        if number not in menu:
            print("Invalid item.")
            return
        print(f"Selected: {menu[number]['name']}")
        confirm = input("Delete this item? (y/n): ").lower()
        if confirm == "y":
            del menu[number]
            print("Food item removed.")
        else:
            print("Deletion cancelled.")
    except ValueError:
        print("Enter a valid item number.")


def admin_menu():
    if not admin_login():
        return
    while True:
        title("ADMIN MENU")
        print("1. View Inventory")
        print("2. Restock Item")
        print("3. Update Price")
        print("4. Add Food Item")
        print("5. Remove Food Item")
        print("6. Return")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            show_inventory()
        elif choice == "2":
            restock_item()
        elif choice == "3":
            update_price()
        elif choice == "4":
            add_food_item()
        elif choice == "5":
            remove_food_item()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")


def help_menu():
    title("HELP")
    print("1. View the menu and choose an item number.")
    print("2. Add the required quantity.")
    print("3. View or modify your order.")
    print("4. Checkout and select a payment method.")
    print("5. The bill is automatically saved after checkout.")


def about_project():
    title("ABOUT THE PROJECT")
    print("Project: Smart Canteen Ordering and Billing System")
    print("Language: Python")
    print("Level: First Year CSE Core")
    print("Concepts: Dictionaries, Functions, Loops, Conditions,")
    print("Exception Handling, File Handling and Datetime.")


def customer_menu(customer_name):
    while True:
        title("CUSTOMER MAIN MENU")
        print("1. Display Food Menu")
        print("2. Search Food")
        print("3. Add Item")
        print("4. View Order")
        print("5. Remove Item")
        print("6. Clear Order")
        print("7. Checkout and Generate Bill")
        print("8. Help")
        print("9. About Project")
        print("10. Return to Start Menu")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_menu()
        elif choice == "2":
            search_food()
        elif choice == "3":
            add_item()
        elif choice == "4":
            view_order()
        elif choice == "5":
            remove_item()
        elif choice == "6":
            clear_order()
        elif choice == "7":
            checkout(customer_name)
        elif choice == "8":
            help_menu()
        elif choice == "9":
            about_project()
        elif choice == "10":
            break
        else:
            print("Invalid choice. Please select 1-10.")


def start_program():
    while True:
        title("WELCOME TO SMART CANTEEN")
        print("1. Customer")
        print("2. Admin")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            customer_name = input("Enter customer name: ").strip()
            if customer_name:
                customer_menu(customer_name)
            else:
                print("Customer name cannot be empty.")
        elif choice == "2":
            admin_menu()
        elif choice == "3":
            print("Thank you for using Smart Canteen!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    start_program()
