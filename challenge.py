class EmailService:
    def send_email(self, user_email):
        print(f"Sending email to {user_email}")

class UserRegistration:
    def __init__(self):
        self.email_service = EmailService()  #  Dependencia directa

    def register_user(self, user_email):
        print("User registered!")
        self.email_service.send_email(user_email)  # Acoplamiento fuerte

# Uso del sistema
registration = UserRegistration()
registration.register_user("user@example.com")


# Tarea Crea una interfaz IEmailService para desacoplar UserRegistration de EmailService.
# Permite cambiar la implementación del servicio de email sin modificar UserRegistration.