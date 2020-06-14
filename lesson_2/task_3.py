number = int(input("Введите порядковый номер месяца: "))

if number >= 12 or number == 0:
    print("Число введено неверно")
    exit()

# со словарем
mounths = {"Зима": [1, 2, 12], "Весна": [3, 4, 5], "Лето": [6, 7, 8], "Осень": [9, 10, 11]}

for key in mounths.keys():
    if number in  mounths.get(key):
        print("Cо словарем: " + key)


# со списком

mounths = ["Зима", "Весна", "Лето", "Осень"]

if number in [1, 2, 12]:
    print("Cо списком: " + mounths[0])
elif number in [3, 4, 5]:
    print("Cо списком: " + mounths[1])
elif number in [6, 7, 8]:
    print("Cо списком: " + mounths[2])
else:
    print("Cо списком: " + mounths[3])
