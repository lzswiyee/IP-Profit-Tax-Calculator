# src/tax_module.py

SYSTEMS = ["УСН 6%", "УСН 15%"]

BENEFITS_DICT = {
    "Без льгот": "NONE",
    "Региональная льгота IT-сектор (УСН 1% / 5%)": "IT",
    "Региональная льгота Social (УСН 2% / 7%)": "SOCIAL",
    "Пониженная ставка региона (УСН 4% / 10%)": "REGIONAL_MID",
}

def get_tax_rate(system):
    if "6" in str(system):
        return 0.06
    return 0.15

def calculate_benefit_discount(base_tax, system, benefit_name, income, profit):
    discount_type = BENEFITS_DICT.get(benefit_name, "NONE")

    if discount_type == "NONE":
        return 0.0

    target_rate = None
    is_usn_6 = "6" in str(system)

    if discount_type == "IT":
        target_rate = 0.01 if is_usn_6 else 0.05
    elif discount_type == "SOCIAL":
        target_rate = 0.02 if is_usn_6 else 0.07
    elif discount_type == "REGIONAL_MID":
        target_rate = 0.04 if is_usn_6 else 0.10

    if target_rate is not None:
        base_rate = get_tax_rate(system)
        rate_diff = max(0.0, base_rate - target_rate)

        if is_usn_6:
            return round(float(income * rate_diff), 2)
        else:
            return round(float(max(0.0, profit) * rate_diff), 2)

    return 0.0
