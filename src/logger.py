from tkinter import messagebox

def generate_report(data, results):
    report = (
        f"=== ОТЧЁТ ИП ===\n"
        f"Система: {data['tax_type']}\n"
        f"Доходы: {data['income']:.2f}\n"
        f"Расходы: {data['expenses']:.2f}\n"
        f"Налоговая база: {results['tax_base']:.2f}\n"
        f"Налог (базовый): {results['tax']:.2f}\n"
        f"----------------\n"
        f"ИТОГО К УПЛАТЕ: {results['total_tax']:.2f}"
    )
    return report

def output_gui(report_text):
    messagebox.showinfo("Результат расчета", report_text)
