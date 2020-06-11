raw_seconds = int(input("Введите время в секундах: "))

for_h= 60 * 60

hours = int(raw_seconds / for_h)
print(hours)

fot_m=int(raw_seconds % for_h)

minutes = int(fot_m / 60)

seconds = int(raw_seconds % 60)

print("{}:{}:{}".format(hours, minutes, seconds))
