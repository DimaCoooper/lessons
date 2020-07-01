class Worker:
    def __init__(self, name,surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):

    def get_full_name(self):
        print(f"Полное имя: {self.name} {self.surname} "+"\n"+f"Должность: {self.position}")


    def get_total_income(self):
        income = sum(self._income.values())

        print(f"Зарплата: {income}")



a = Position("Dima", "Cooper", "IT", 300, 50)

a.get_full_name()

a.get_total_income()