list = [3, "string", True, [1, 4], {"1": "value_1", "2": "value_2"}]
num=0
for i in list:
    print("Элемент {} = {}".format(num, i),
          "\n",
          "Тип элемента = {}".format(type(i)),
          "\n")
    num+=1