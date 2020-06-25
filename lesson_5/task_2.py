with open("new.txt", "r",encoding="utf-8") as file:
    i = 1
    for line in file:
        numbers = len(line.split())
        print(f"Количество слов в строке {i}: {numbers}")
        i += 1