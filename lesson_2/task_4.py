string = str(input("Введите сроку: "))

a = string.split()
print(a)

i = 1
for word in a:
    if len(word) <= 10:
        print(f" Строка {i}: {word}")
        i += 1
    else:
        i += 1
        word = word[0:10]
        print(f" Строка {i}: {word}")
