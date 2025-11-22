# notificador.py
from datetime import datetime

# Clase base para las notificaciones
class Notifier:

    def send(self, order_data):
        pass


# Notificación por correo
class EmailNotifier(Notifier):
    def send(self, order_data):
        # Sacamos los datos del pedido
        customer = order_data['customer']
        order_id = order_data['order_id']
        total = order_data['total']

        # Hago el mensaje
        message = f"Estimado {customer['name']}, su pedido #{order_id} por ${total} ha sido confirmado."
        print(f"📧 EMAIL enviado a {customer['email']}")
        print(f"   Asunto: Confirmación de Pedido #{order_id}")
        print(f"   Mensaje: {message}\n")

        # Regreso la Info
        return {
            'type': 'email',
            'to': customer['email'],
            'message': message,
            'timestamp': datetime.now().isoformat()
        }


# Notificación por SMS
class SmsNotifier(Notifier):
    def send(self, order_data):
        customer = order_data['customer']
        order_id = order_data['order_id']
        total = order_data['total']

        message = f"Pedido #{order_id} confirmado. Total: ${total}. Gracias por su compra!"
        print(f"📱 SMS enviado a {customer['phone']}")
        print(f"   Mensaje: {message}\n")

        return {
            'type': 'sms',
            'to': customer['phone'],
            'message': message,
            'timestamp': datetime.now().isoformat()
        }


# Notificación tipo push
class PushNotifier(Notifier):
    def send(self, order_data):
        customer = order_data['customer']
        order_id = order_data['order_id']
        total = order_data['total']

        message = f"¡Pedido confirmado! #{order_id} - ${total}"
        print(f"🔔 PUSH enviada al dispositivo {customer['device_id']}")
        print(f"   Mensaje: {message}\n")

        return {
            'type': 'push',
            'to': customer['device_id'],
            'message': message,
            'timestamp': datetime.now().isoformat()
        }
