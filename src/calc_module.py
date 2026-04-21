import tax_module
from utils import normalize


def process_calculation(data):
    profit = tax_module.calc_profit(data['income'], data['expenses'])

    if data['tax_type'] == "УСН 6%":
        tax_base = data['income']
        initial_tax = tax_module.calc_tax_6(data['income'])
    else:
        tax_base = normalize(profit)
        initial_tax = tax_module.calc_tax_15(tax_base)

    tax_after_benefits = tax_module.apply_benefits(initial_tax, data['benefits'])
    total_tax = tax_module.apply_fees(tax_after_benefits, data['fees'])

    return {
        "tax_base": tax_base,
        "tax": initial_tax,
        "total_tax": total_tax,
        "profit": profit
    }
