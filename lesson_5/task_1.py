list = []
while True:
    item = str(input("введите строку: "))
    if item is not '':
        list.append(item)
    else:
        break


with open("new_1.txt", "w",encoding="utf-8") as file:
    for i in list:
        file.writelines(i + "\n")


