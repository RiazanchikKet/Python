def is_year_lip(n):
    if n % 4 == 0:
        return True
    else:
        return False


year = int(input("Введите год: "))
result = is_year_lip(year)
print(f"год {year}: {result}")
