import pytest

from src.calc_module import calculate_tax
from src.tax_module import get_tax_rate
from src.utils import format_currency

def test_calculation_logic():
    assert calculate_tax(1000, 0.06) == 60
    assert calculate_tax(0, 0.06) == 0

def test_tax_rates():
    assert get_tax_rate('USN_income') == 0.06
    assert get_tax_rate('USN_profit') == 0.15

def test_formatting():
    assert format_currency(100.5) == "100.50 руб."
