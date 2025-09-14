# customer.py
class Customer:
    def __init__(self, cid: str, name: str, phone: str):
        self.cid = cid
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"{self.cid} | {self.name} | {self.phone}"
