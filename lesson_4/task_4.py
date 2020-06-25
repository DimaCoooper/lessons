def new_func():

    list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

    new_list1 = []

################

    for i in list:
        if i not in new_list1:
            new_list1.append(i)

################

    new_list2 = [item for item in list if item not in new_list1]

    print(f"new_list1 = {new_list1}")
    print(f"new_list2 = {new_list2}")

    # не очень понятно почему не работает с генератором :(

def main():

    new_func()


if __name__ == "__main__":
    main()
