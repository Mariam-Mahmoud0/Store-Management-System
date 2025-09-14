# sale.py
from datetime import datetime

class Sale:
    def __init__(self, cid, pid, quantity, total, timestamp=None):
        self.cid = cid
        self.pid = pid
        self.quantity = quantity
        self.total = total
        self.timestamp = timestamp or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"{self.timestamp} | Customer {self.cid} bought {self.quantity} of {self.pid} | Total: ${self.total:.2f}"
