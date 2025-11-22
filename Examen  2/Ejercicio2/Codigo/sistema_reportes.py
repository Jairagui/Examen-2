# sistema_reportes.py
from datetime import datetime
import json

from tipos_reporte import (
    GeneradorReporteVentas,
    GeneradorReporteInventario,
    GeneradorReporteFinanciero,
)


class ReportSystem:
    def __init__(self):
        self.reports_generated = []

    # Fábrica para el tipo de reporte
    def _crear_generador_reporte(self, report_type):
        report_type = str(report_type).lower()

        if report_type == 'sales':
            return GeneradorReporteVentas()
        elif report_type == 'inventory':
            return GeneradorReporteInventario()
        elif report_type == 'financial':
            return GeneradorReporteFinanciero()
        else:
            print("⚠️ Tipo de reporte desconocido:", report_type)
            return None

    def generate_report(self, report_type, data, output_format, delivery_method):

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Usamos el generador según el tipo de reporte
        generador = self._crear_generador_reporte(report_type)
        if generador is None:
            return None

        report_content = generador.generar(data, timestamp)

        # Formatear según el formato de salida
        formatted_report = ""

        if output_format == 'pdf':
            formatted_report = f"[PDF FORMAT]\n{report_content}\n[END PDF]"
            print("📄 Generando reporte en formato PDF...")

        elif output_format == 'excel':
            formatted_report = f"[EXCEL FORMAT]\n{report_content}\n[END EXCEL]"
            print("📊 Generando reporte en formato Excel...")

        elif output_format == 'html':
            formatted_report = f"<html><body><pre>{report_content}</pre></body></html>"
            print("🌐 Generando reporte en formato HTML...")


        if delivery_method == 'email':
            print("📧 Enviando reporte por email...")
            print("   Destinatario: admin@company.com")

        elif delivery_method == 'download':
            filename = f"report_{report_type}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{output_format}"
            print(f"💾 Reporte disponible para descarga: {filename}")

        elif delivery_method == 'cloud':
            print("☁️  Subiendo reporte a la nube...")
            print(f"   URL: https://cloud.company.com/reports/{report_type}")


        self.reports_generated.append({
            'type': report_type,
            'format': output_format,
            'delivery': delivery_method,
            'timestamp': timestamp
        })

        print("\n✅ Reporte generado exitosamente\n")
        print(formatted_report)
        print("\n" + "=" * 60 + "\n")

        return formatted_report

    def get_report_history(self):
        return self.reports_generated
