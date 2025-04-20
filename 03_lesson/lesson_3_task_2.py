from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy 10", "+7 900 800 32-32"),
    Smartphone("Xiaomi", "Not Pro 8", "+ 7 900 100 40-30"),
    Smartphone("iPhone", "16 Pro", "+7 900 300 90-90"),
    Smartphone("Motorolla", "RAZR", "+7 900 400 90-80"),
    Smartphone("Huawei", "pura 70 Pro", "+7 900 500 70-60")
]

for smart in catalog:
    print(f"{smart.maker} - {smart.model}. {smart.number}")
