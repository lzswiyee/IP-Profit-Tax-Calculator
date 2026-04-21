from utils import normalize

def calc_profit(income, expenses):
    return income - expenses

def calc_tax_6(income):
    return income * 0.06

def calc_tax_15(profit):
    return normalize(profit) * 0.15

def apply_benefits(tax, benefits):
    return normalize(tax - benefits)

def apply_fees(tax, fees):
    return normalize(tax - fees)

