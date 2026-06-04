def get_user_input():
    income = float(input("Введите доход: "))
    expenses = float(input("Введите расходы: "))

    while True:
        choice = input("Выберите систему (УСН 6% / УСН 15%): ").strip()
        if choice in ["6", "15", "УСН 6%", "УСН 15%"]:
            system = "УСН 6%" if "6" in choice else "УСН 15%"
            break
        print("Ошибка! Введите только 6 или 15.")

    benefits = input("Введите льготу (или 'Без льгот'): ").strip()
    contributions = float(input("Введите взносы: "))
    return income, expenses, system, benefits, contributions
