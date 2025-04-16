from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy 10", "+7 900 800 32-32"),
    Smartphone("Xiaomi", "Not Pro 8", "+ 7 900 100 40-30"),
    Smartphone("iPhone", "16 Pro", "+7 900 300 90-90")
]

for smart in catalog:
    print(f"{smart.maker} - {smart.model}. {smart.number}")
