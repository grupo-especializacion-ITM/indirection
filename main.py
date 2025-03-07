from abc import ABC, abstractmethod

# ✅ Interfaz para permitir múltiples formas de pago
class IPaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# ✅ Implementación de pago con tarjeta
class CardPaymentProcessor(IPaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing card payment of ${amount}")

# ✅ Implementación de pago con PayPal
class PayPalPaymentProcessor(IPaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

# ✅ OrderService ahora depende de la abstracción en lugar de una implementación concreta
class OrderService:
    def __init__(self, payment_processor: IPaymentProcessor):
        self.payment_processor = payment_processor  # ✅ Inyección de dependencia

    def place_order(self, amount):
        print("Order placed!")
        self.payment_processor.process_payment(amount)  # ✅ Sin acoplamiento fuerte

# Uso del sistema
order_service1 = OrderService(CardPaymentProcessor())
order_service1.place_order(100)

order_service2 = OrderService(PayPalPaymentProcessor())
order_service2.place_order(200)