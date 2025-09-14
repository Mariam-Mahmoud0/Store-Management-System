# main.py
from store import Store

store = Store()

while True:
    print("\n===== Store Management Menu =====")
    print("1. Add Product")
    print("2. Add Customer")
    print("3. Sell Product")
    print("4. List Products")
    print("5. List Sales")
    print("6. Clear All Data")
    print("7. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            pid = input("Enter product ID: ")
            name = input("Enter product name: ")
            price = float(input("Enter price: "))
            qty = int(input("Enter quantity: "))
            try:
                store.add_product(pid, name, price, qty)
            except Exception as e:
                print(f"⚠️ Could not add product: {e}")

        elif choice == "2":
            cid = input("Enter customer ID: ")
            name = input("Enter customer name: ")
            phone = input("Enter phone number: ")
            try:
                store.add_customer(cid, name, phone)
            except Exception as e:
                print(f"⚠️ Could not add customer: {e}")

        elif choice == "3":
            pid = input("Enter product ID: ")
            cid = input("Enter customer ID: ")
            qty = int(input("Enter quantity: "))
            try:
                store.sell_product(pid, cid, qty)
            except Exception as e:
                print(f"⚠️ Sale failed: {e}")

        elif choice == "4":
            store.list_products()

        elif choice == "5":
            store.list_sales()

        elif choice == "6":
            confirm = input("Are you sure? This will delete all data! (yes/no): ")
            if confirm.lower() == "yes":
                store.clear_data()
            else:
                print("❌ Clear data canceled.")

        elif choice == "7":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice, please try again.")

    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")
