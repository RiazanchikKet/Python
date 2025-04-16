
def month_to_season():
    month = int(input("Введите номер месяца: "))
    if month >= 1 and month <= 2 or month == 12:
        return "Зима"
    elif month >= 3 and month <= 5:
        return "Весна"
    elif month >= 6 and month <= 8:
        return "Лето"
    elif month <= 9 and month >= 11:
        return "Осень"
    else:
        return "Указан неверный номер месяца!"


print(month_to_season())
