# main.py

import json
from sistema_notificaciones import OrderNotificationSystem

if __name__ == "__main__":
    #  sistema de notificaciones
    system = OrderNotificationSystem()

    # Pedido 1: Cliente premium (todos los canales)
    order1 = {
        'order_id': 'ORD-001',
        'customer': {
            'name': 'Ana García',
            'email': 'ana.garcia@email.com',
            'phone': '+34-600-123-456',
            'device_id': 'DEVICE-ABC-123'
        },
        'total': 150.50
    }

    # Enviamos email, sms y push
    system.process_order(order1, ['email', 'sms', 'push'])

    # Pedido 2: Cliente estándar (solo email)
    order2 = {
        'order_id': 'ORD-002',
        'customer': {
            'name': 'Carlos Ruiz',
            'email': 'carlos.ruiz@email.com',
            'phone': '+34-600-789-012',
            'device_id': 'DEVICE-XYZ-789'
        },
        'total': 75.00
    }

    #mando email
    system.process_order(order2, ['email'])

    # Mostrar historial al final
    print("\n" + "="*50)
    print("HISTORIAL DE NOTIFICACIONES")
    print("="*50)
    history = system.get_notification_history()
    print(json.dumps(history, indent=2, ensure_ascii=False))
