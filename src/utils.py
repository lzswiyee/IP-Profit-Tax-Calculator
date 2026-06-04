def format_currency(value):
    return f"{int(value):,}".replace(",", ".") + " руб."
