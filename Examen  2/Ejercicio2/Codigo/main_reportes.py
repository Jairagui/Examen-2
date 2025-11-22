# main_reportes.py
from sistema_reportes import ReportSystem
import json

if __name__ == "__main__":
    system = ReportSystem()

    # Reporte de ventas
    sales_data = {
        'period': 'Enero 2024',
        'sales': [
            {'product': 'Laptop HP', 'amount': 899.99},
            {'product': 'Mouse Logitech', 'amount': 25.50},
            {'product': 'Teclado Mecánico', 'amount': 120.00},
            {'product': 'Monitor LG 24"', 'amount': 199.99}
        ]
    }

    system.generate_report('sales', sales_data, 'pdf', 'email')

    # Reporte de inventario
    inventory_data = {
        'items': [
            {'name': 'Laptop HP', 'category': 'Computadoras', 'quantity': 15},
            {'name': 'Mouse Logitech', 'category': 'Accesorios', 'quantity': 50},
            {'name': 'Teclado Mecánico', 'category': 'Accesorios', 'quantity': 30},
            {'name': 'Monitor LG', 'category': 'Pantallas', 'quantity': 20}
        ]
    }

    system.generate_report('inventory', inventory_data, 'excel', 'download')

    # Reporte financiero
    financial_data = {
        'income': 50000.00,
        'expenses': 32000.00
    }

    system.generate_report('financial', financial_data, 'html', 'cloud')

    # Mostrar historial
    print("\nHISTORIAL DE REPORTES GENERADOS:")
    print(json.dumps(system.get_report_history(), indent=2, ensure_ascii=False))
