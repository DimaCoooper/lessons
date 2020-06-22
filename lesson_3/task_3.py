def minimal(a, b, c):
    list = [a,b ,c]

    value = min(list)
    print(value)

    index = list.index(min(list))

    print(index)

    c = list.pop(index)

    print(c)

    print(list)

minimal(2,99,3)