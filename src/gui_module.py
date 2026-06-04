import tkinter as tk
from tkinter import ttk, messagebox
from calc_module import calculate_ip_tax
from tax_module import BENEFITS_DICT, SYSTEMS
from utils import format_currency
from logger import logger


class TaxCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("IP Tax Calculator")
        self.root.geometry("400x380")
        self.root.resizable(False, False)

        frame = tk.Frame(root)
        frame.pack(padx=20, pady=15, fill="both", expand=True)

        self.val_income = tk.StringVar(value="0 руб.")
        self.val_expenses = tk.StringVar(value="0 руб.")
        self.val_contributions = tk.StringVar(value="0 руб.")

        self.val_income.trace_add("write", lambda *args: self.format_input_mask(self.entry_income, self.val_income))
        self.val_expenses.trace_add("write",
                                    lambda *args: self.format_input_mask(self.entry_expenses, self.val_expenses))
        self.val_contributions.trace_add("write", lambda *args: self.format_input_mask(self.entry_contributions,
                                                                                       self.val_contributions))

        tk.Label(frame, text="Доходы за год:").pack(anchor="w", pady=2)
        self.entry_income = tk.Entry(frame, textvariable=self.val_income)
        self.entry_income.pack(fill="x", pady=2)
        self.entry_income.bind("<FocusIn>", lambda e: self.clear_placeholder(self.entry_income))
        self.entry_income.bind("<FocusOut>", lambda e: self.restore_placeholder(self.entry_income))

        tk.Label(frame, text="Расходы за год:").pack(anchor="w", pady=2)
        self.entry_expenses = tk.Entry(frame, textvariable=self.val_expenses)
        self.entry_expenses.pack(fill="x", pady=2)
        self.entry_expenses.bind("<FocusIn>", lambda e: self.clear_placeholder(self.entry_expenses))
        self.entry_expenses.bind("<FocusOut>", lambda e: self.restore_placeholder(self.entry_expenses))

        tk.Label(frame, text="Страховые взносы:").pack(anchor="w", pady=2)
        self.entry_contributions = tk.Entry(frame, textvariable=self.val_contributions)
        self.entry_contributions.pack(fill="x", pady=2)
        self.entry_contributions.bind("<FocusIn>", lambda e: self.clear_placeholder(self.entry_contributions))
        self.entry_contributions.bind("<FocusOut>", lambda e: self.restore_placeholder(self.entry_contributions))

        tk.Label(frame, text="Система налогообложения:").pack(anchor="w", pady=2)
        self.system_combo = ttk.Combobox(frame, values=SYSTEMS, state="readonly")
        self.system_combo.set("УСН 6%")
        self.system_combo.pack(fill="x", pady=2)

        tk.Label(frame, text="Налоговая льгота:").pack(anchor="w", pady=2)
        self.benefit_combo = ttk.Combobox(frame, values=list(BENEFITS_DICT.keys()), state="readonly")
        self.benefit_combo.set("Без льгот")
        self.benefit_combo.pack(fill="x", pady=2)

        self.btn_calc = tk.Button(frame, text="Рассчитать", command=self.run_calculation)
        self.btn_calc.pack(fill="x", pady=15)

        self.lbl_result = tk.Label(frame, text="Итого к уплате: 0 руб.", font=("Arial", 10, "bold"))
        self.lbl_result.pack(pady=5)

    def format_input_mask(self, entry, text_var):
        current_text = text_var.get()
        digits = "".join([c for c in current_text if c.isdigit()])

        if not digits:
            return

        val_int = int(digits)
        formatted = f"{val_int:,}".replace(",", ".") + " руб."

        if current_text != formatted:
            old_pos_from_end = len(current_text) - entry.index(tk.INSERT)
            text_var.set(formatted)
            new_pos = max(0, len(formatted) - old_pos_from_end)
            if new_pos > len(formatted) - 5:
                new_pos = len(formatted) - 5
            entry.icursor(new_pos)

    def clear_placeholder(self, entry):
        if entry.get() == "0 руб.":
            entry.delete(0, tk.END)

    def restore_placeholder(self, entry):
        text = entry.get().replace(" руб.", "").strip()
        if text == "" or text == "0":
            entry.delete(0, tk.END)
            entry.insert(0, "0 руб.")

    def parse_value(self, text_var):
        clean_text = "".join([c for c in text_var.get() if c.isdigit()])
        return float(clean_text) if clean_text else 0.0

    def run_calculation(self):
        try:
            income = self.parse_value(self.val_income)
            expenses = self.parse_value(self.val_expenses)
            contributions = self.parse_value(self.val_contributions)

            if income == 0:
                messagebox.showwarning("Внимание", "Поле «Доходы за год» является обязательным для ввода")
                return
            if expenses == 0:
                messagebox.showwarning("Внимание",
                                       "Поле «Расходы за год» является обязательным для ввода")
                return

            system = self.system_combo.get()
            benefit_name = self.benefit_combo.get()

            final_tax = calculate_ip_tax(income, expenses, system, benefit_name, contributions)

            self.lbl_result.config(text=f"Итого к уплате: {format_currency(final_tax)}")
            logger.info(f"Расчет: налог {format_currency(final_tax)}")

        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка при расчете: {e}")
