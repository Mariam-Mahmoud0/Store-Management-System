# store.py
import csv
from product import Product
from customer import Customer
from sale import Sale

class Store:
    def __init__(self):
        self.products = {}
        self.customers = {}
        self.sales = []
        self.load_data()

    # ---------- Products ----------
    def add_product(self, pid, name, price, quantity):
        if pid in self.products:
            self.products[pid].update_stock(quantity)
            print(f"Added new product: {name}.")
        else:
            self.products[pid] = Product(pid, name, price, quantity)
            print(f"Updated stock for {name} (+{quantity}).")
        self.save_products()

    # ---------- Customers ----------
    def add_customer(self, cid, name, phone):
        if cid in self.customers:
            raise ValueError("Customer already exists")
        self.customers[cid] = Customer(cid, name, phone)
        print(f"Added new customer: {name} (ID: {cid}).")
        self.save_customers()

    # ---------- Sales ----------
    def sell_product(self, pid, cid, quantity):
        if pid not in self.products:
            raise ValueError("Product not found")
        if cid not in self.customers:
            raise ValueError("Customer not found")
        product = self.products[pid]
        if product.quantity < quantity:
            raise ValueError("Not enough stock available")
        product.update_stock(-quantity)
        total = product.price * quantity
        sale = Sale(cid, pid, quantity, total)
        self.sales.append(sale)
        print(f"Sale completed: {self.customers[cid].name} bought {quantity} x {product.name}")
        self.save_sales()

    # ---------- Listing ----------
    def list_products(self):
        print("\n--- Product List ---")
        if not self.products:
            print("No products in the store yet.")
            return
        print(f"{'ID':<5} | {'Name':<15} | {'Price':<7} | {'Qty':<5}")
        print("-" * 40)
        for p in self.products.values():
            print(f"{p.pid:<5} | {p.name:<15} | ${p.price:<7.2f} | {p.quantity:<5}")

    def list_sales(self):
        print("\n--- Sales Records ---")
        if not self.sales:
            print("No sales yet.")
            return
        total_revenue = 0
        for s in self.sales:
            print(s)
            total_revenue += s.total
        print(f"\nTotal Revenue: ${total_revenue:.2f}")

    # ---------- Save / Load ----------
    def save_products(self):
        with open("products.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["pid", "name", "price", "quantity"])
            for p in self.products.values():
                writer.writerow([p.pid, p.name, p.price, p.quantity])

    def save_customers(self):
        with open("customers.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["cid", "name", "phone"])
            for c in self.customers.values():
                writer.writerow([c.cid, c.name, c.phone])

    def save_sales(self):
        with open("sales.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["cid", "pid", "quantity", "total", "timestamp"])
            for s in self.sales:
                writer.writerow([s.cid, s.pid, s.quantity, s.total, s.timestamp])

    def load_data(self):
        try:
            with open("products.csv") as f:
                reader = csv.DictReader(f)
                for r in reader:
                    self.products[r["pid"]] = Product(r["pid"], r["name"], float(r["price"]), int(r["quantity"]))
        except FileNotFoundError:
            pass

        try:
            with open("customers.csv") as f:
                reader = csv.DictReader(f)
                for r in reader:
                    self.customers[r["cid"]] = Customer(r["cid"], r["name"], r["phone"])
        except FileNotFoundError:
            pass

        try:
            with open("sales.csv") as f:
                reader = csv.DictReader(f)
                for r in reader:
                    self.sales.append(Sale(r["cid"], r["pid"], int(r["quantity"]), float(r["total"]), r["timestamp"]))
        except FileNotFoundError:
            pass

    # ---------- Clear Data ----------
    def clear_data(self):
        self.products.clear()
        self.customers.clear()
        self.sales.clear()
        open("products.csv", "w").close()
        open("customers.csv", "w").close()
        open("sales.csv", "w").close()
        print("✅ All store data has been cleared.")
