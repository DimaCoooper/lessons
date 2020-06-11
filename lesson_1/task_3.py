a = int(input("Введите число: "))

first = "{}".format(a)
second = "{}{}".format(a,a)
third = "{}{}{}".format(a,a,a)

sum = str(int(first) + int(second) + int(third))
print("Cумма равна: {}".format(sum))
