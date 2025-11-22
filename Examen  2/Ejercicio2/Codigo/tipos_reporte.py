# tipos_reporte.py
# Clases para generar el contenido según el tipo de reporte


class GeneradorReporte:

    def generar(self, data, timestamp):
        report_content = ""
        report_content += "=" * 60 + "\n"
        report_content += f"           {self._nombre_reporte()}\n"
        report_content += "=" * 60 + "\n"
        report_content += f"Fecha de generación: {timestamp}\n\n"
        report_content += self._contenido(data)
        return report_content

    # Estos métodos los sobreescriben las subclases
    def _nombre_reporte(self):
        return ""

    def _contenido(self, data):
        return ""


class GeneradorReporteVentas(GeneradorReporte):
    def _nombre_reporte(self):
        return "REPORTE DE VENTAS"

    def _contenido(self, data):
        report_content = ""

        total_sales = sum(item['amount'] for item in data['sales'])
        report_content += f"Total de ventas: ${total_sales:.2f}\n"
        report_content += f"Número de transacciones: {len(data['sales'])}\n"
        report_content += f"Periodo: {data['period']}\n\n"

        report_content += "Detalle de ventas:\n"
        report_content += "-" * 60 + "\n"
        for sale in data['sales']:
            report_content += f"  • Producto: {sale['product']} - ${sale['amount']:.2f}\n"

        return report_content


class GeneradorReporteInventario(GeneradorReporte):
    def _nombre_reporte(self):
        return "REPORTE DE INVENTARIO"

    def _contenido(self, data):
        report_content = ""

        total_items = sum(item['quantity'] for item in data['items'])
        report_content += f"Total de productos: {total_items}\n"
        report_content += f"Categorías: {len(set(item['category'] for item in data['items']))}\n\n"

        report_content += "Inventario actual:\n"
        report_content += "-" * 60 + "\n"
        for item in data['items']:
            report_content += f"  • {item['name']} ({item['category']}): {item['quantity']} unidades\n"

        return report_content


class GeneradorReporteFinanciero(GeneradorReporte):
    def _nombre_reporte(self):
        return "REPORTE FINANCIERO"

    def _contenido(self, data):
        report_content = ""

        report_content += f"Ingresos: ${data['income']:.2f}\n"
        report_content += f"Gastos: ${data['expenses']:.2f}\n"
        report_content += f"Balance: ${data['income'] - data['expenses']:.2f}\n"

        return report_content
