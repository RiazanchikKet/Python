
def square(n):
    import math
    return math.ceil(n * n)


num = float(input("Введите число: "))
resalt = square(num)
print(f"Площадь квадрата от числа {num} = {resalt}")
