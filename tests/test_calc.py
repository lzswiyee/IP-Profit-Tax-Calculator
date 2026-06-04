import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from calc_module import calculate_ip_tax

class TestTaxCalculator(unittest.TestCase):

    def test_usn_6_without_benefits(self):
        # Доход: 1 000 000, Расход: 0, Система: УСН 6%, Льгота: Без льгот, Взносы: 0
        # Налог должен быть: 1 000 000 * 0.06 = 60 000
        result = calculate_ip_tax(1000000, 0, "УСН 6%", "Без льгот", 0)
        self.assertEqual(result, 60000.0)

    def test_usn_6_with_contributions(self):
        # Налог: 60 000 - Взносы: 10 000 = 50 000
        result = calculate_ip_tax(1000000, 0, "УСН 6%", "Без льгот", 10000)
        self.assertEqual(result, 50000.0)

    def test_usn_15_without_benefits(self):
        # Прибыль: 1 000 000 - 400 000 = 600 000
        # Налог: 600 000 * 0.15 = 90 000
        result = calculate_ip_tax(1000000, 400000, "УСН 15%", "Без льгот", 0)
        self.assertEqual(result, 90000.0)

    def test_it_benefit_usn_6(self):
        # Налог: 1 000 000 * 0.01 = 10 000
        result = calculate_ip_tax(1000000, 0, "УСН 6%", "Региональная льгота IT-сектор (УСН 1% / 5%)", 0)
        self.assertEqual(result, 10000.0)

    def test_negative_tax_protection(self):
        # Базовый налог 60 000, а взносов ввели на 70 000. Результат должен быть 0, а не -10 000
        result = calculate_ip_tax(1000000, 0, "УСН 6%", "Без льгот", 70000)
        self.assertEqual(result, 0.0)

if __name__ == '__main__':
    unittest.main()
