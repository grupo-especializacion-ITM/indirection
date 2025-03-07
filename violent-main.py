class PaymentProcessor:
    def process_payment(self, amount):
        print(f"Processing payment of ${amount}")

class OrderService:
    def __init__(self):
        self.payment_processor = PaymentProcessor()  # Dependencia directa

    def place_order(self, amount):
        print("Order placed!")
        self.payment_processor.process_payment(amount)  # Acoplamiento fuerte

# Uso del sistema
order_service = OrderService()
order_service.place_order(100)