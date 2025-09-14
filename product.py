# product.py
class Product:
    def __init__(self, pid, name: str, price: float, quantity: int):
        if price < 0:
            raise ValueError("Price must be >= 0")
        if quantity < 0:
            raise ValueError("Quantity must be >= 0")
        self.pid = pid
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_stock(self, new_stock: int):
        if self.quantity + new_stock < 0:
            raise ValueError("Resulting quantity must be >= 0")
        self.quantity += int(new_stock)

    def __str__(self):
        return f"{self.pid} | {self.name} | ${self.price:.2f} | {self.quantity}"
