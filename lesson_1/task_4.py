a = int(input("Введите число: "))
len = len(str(a))

number = 0
i=1
while i <= len:
    b = a % 10
    a = a // 10
    if b > number:
        number = b
        i += 1
    else:
        i += 1
print(number)
