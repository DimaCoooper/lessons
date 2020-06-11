dohod = int(input("Доход: "))
rashod = int(input("Расход: "))

if dohod < rashod:
    diff = rashod - dohod
    print("Убыток равен: " + str(diff))
elif dohod == rashod:
    print("вышли 0")
else:
    diff = dohod - rashod
    print("рентабильность: {}".format(diff))
    emp = int(input("Количество сотрудников: "))
    diff_on_emp = diff / emp
    print("Прибыль на одно сотрудника составляет {}.".format(diff_on_emp))

