def new_func():

    list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

    new_list1 = []

################

    for i in list:
        if i not in new_list1:
            new_list1.append(i)

################

    new_list2 = (item for item in list)

    #print(type(new_list2))
    #print([new_list2])

    #print(f"new_list1 = {new_list1}")
    #print(f"new_list2 = {new_list2}")

    yield new_list2
    # не очень понятно почему не работает с генератором :(

def main():

    for i in new_func():
        print(i)
    print(type(new_func()))
    print(list(new_func()))

if __name__ == "__main__":
    main()
