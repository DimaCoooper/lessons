

bedolagi = []

with open("users.txt", "r",encoding="utf-8") as file:

    a = str(file.count('\n'))
    print(a)


    for user in file:
        user = user.split()
        sum += int(user[1])
        if int(user[1]) <= 20000:
            bedolagi.append(user[0])



print(sum)
print(bedolagi)