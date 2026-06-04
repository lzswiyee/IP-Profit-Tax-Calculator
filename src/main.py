import tkinter as tk
from gui_module import TaxCalculatorApp
from logger import logger

def main():
    try:
        logger.info("Запуск приложения IP-Profit-Tax-Calculator (Интерфейс Tkinter)")
        root = tk.Tk()
        app = TaxCalculatorApp(root)
        root.mainloop()
    except Exception as e:
        logger.error(f"Критическая ошибка приложения: {e}")

if __name__ == "__main__":
    main()