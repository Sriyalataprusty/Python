import qrcode
import os
from urllib.parse import quote
from menu import Menu
class MoneyCounter:
    currency = "rupees"
    
    def __init__(self):
        self.money_received = 0
        self.tip = 0
        
    def report(self):
        print(f"Money received = {self.money_received}, tip = {self.tip}.")
        
    def upi_payment(self,order):
        menu = Menu()
        self.order = menu.find_drink(order)
        cost = self.order.cost
        coffee = self.order.name
        name = "Sriyalata Prusty"
        note = f"for buying {coffee}"
        upi_url = (f"upi://pay?"
                   f"pa=9337435181-2@axl&"
                   f"pn={quote(name)}&"
                   f"tn={quote(note)}&"
                   f"am={cost}&"
                   f"cu=INR"
                   )
        qr = qrcode.make(upi_url)
        qr.save("my_qr.jpg")
        self.money_received += cost
        os.startfile("my_qr.jpg")
        return True
    

if __name__ == "__main__":
    payment = MoneyCounter()
    payment.upi_payment("latte")