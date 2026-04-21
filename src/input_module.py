import tkinter as tk
from tkinter import messagebox

def get_data_gui():
    user_data = {}

    def on_submit():
        try:
            user_data['income'] = float(ent_income.get())
            user_data['expenses'] = float(ent_expenses.get())
            user_data['benefits'] = float(ent_benefits.get())
            user_data['fees'] = float(ent_fees.get())
            user_data['tax_type'] = var_tax.get()
            root.destroy()
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректные числа!")

    root = tk.Tk()
    root.title("Налоги ИП")

    # Поля ввода
    tk.Label(root, text="Доход:").grid(row=0, column=0)
    ent_income = tk.Entry(root)
    ent_income.grid(row=0, column=1)

    tk.Label(root, text="Расходы:").grid(row=1, column=0)
    ent_expenses = tk.Entry(root)
    ent_expenses.grid(row=1, column=1)

    tk.Label(root, text="Льготы:").grid(row=2, column=0)
    ent_benefits = tk.Entry(root)
    ent_benefits.grid(row=2, column=1)

    tk.Label(root, text="Взносы:").grid(row=3, column=0)
    ent_fees = tk.Entry(root)
    ent_fees.grid(row=3, column=1)

    # Выбор системы
    var_tax = tk.StringVar(value="УСН 6%")
    tk.Radiobutton(root, text="УСН 6%", variable=var_tax, value="УСН 6%").grid(row=4, column=0)
    tk.Radiobutton(root, text="УСН 15%", variable=var_tax, value="УСН 15%").grid(row=4, column=1)

    tk.Button(root, text="Рассчитать", command=on_submit).grid(row=5, columnspan=2)

    root.mainloop()
    return user_data
