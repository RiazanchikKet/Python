class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def printName(self):
        return f"Имя: {self.first_name}"

    def printLastname(self):
        return f"Фамилия: {self.last_name}"

    def printFull(self):
        return f"Имя и Фамилия: {self.first_name} {self.last_name}"
