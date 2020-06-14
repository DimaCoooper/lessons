list = [10, 11, 22, 33, 44, 55, 66, 77, 88, 99, 8]
half = int(len(list) / 2)


j = 0
for i in range(half):

    list[j], list[j + 1] = list[j + 1], list[j]
    j += 2


print(list)






