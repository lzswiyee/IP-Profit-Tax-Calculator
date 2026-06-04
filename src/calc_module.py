from tax_module import get_tax_rate, calculate_benefit_discount


def calculate_ip_tax(income, expenses, system, benefit_name, contributions):
    rate = get_tax_rate(system)
    profit = income - expenses

    is_usn_6 = "6" in str(system)

    if is_usn_6:
        base_tax = income * rate
    else:
        base_tax = max(0.0, profit) * rate

    benefit_amount = calculate_benefit_discount(base_tax, system, benefit_name, income, profit)

    tax = base_tax - contributions - benefit_amount

    return max(0.0, round(tax, 2))