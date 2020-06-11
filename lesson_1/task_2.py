raw_seconds = int(input("Введите время в секундах: "))

hours = int(raw_seconds / 3600)

fot_m=int(raw_seconds % 3600)
minutes = int(fot_m / 60)

seconds = int(raw_seconds % 60)

print("{}:{}:{}".format(hours, minutes, seconds))
