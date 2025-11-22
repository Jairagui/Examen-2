# fabrica_notificadores.py
# Veo que tipo de notificacion es
from notificador import EmailNotifier, SmsNotifier, PushNotifier

class NotificationFactory:
    def create_notifier(self, notif_type):

        notif_type = str(notif_type).lower()
        # Depende el tipo es la clase que se regersa
        if notif_type == 'email':
            return EmailNotifier()
        elif notif_type == 'sms':
            return SmsNotifier()
        elif notif_type == 'push':
            return PushNotifier()
        else:
            print(f"⚠️ Tipo de notificación desconocido: {notif_type}")
            return None
