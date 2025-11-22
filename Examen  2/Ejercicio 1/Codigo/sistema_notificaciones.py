# sistema_notificaciones.py
import json
from fabrica_notificadores import NotificationFactory

class OrderNotificationSystem:
    def __init__(self):
        self.notifications_sent = []
        self.factory = NotificationFactory()

    def process_order(self, order_data, notification_types):

        # los datos del pedido
        order_id = order_data['order_id']
        customer = order_data['customer']
        total = order_data['total']

        # la info del pedido
        print(f"\n{'='*50}")
        print(f"Procesando pedido #{order_id}")
        print(f"Cliente: {customer['name']}")
        print(f"Total: ${total}")
        print(f"{'='*50}\n")

        for notif_type in notification_types:
            notifier = self.factory.create_notifier(notif_type)
            if notifier is None:
                continue
            notification = notifier.send(order_data)

            self.notifications_sent.append(notification)

    def get_notification_history(self):

        return self.notifications_sent
