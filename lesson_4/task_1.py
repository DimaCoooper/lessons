from sys import argv

script_name, hours, stavka, bonus = argv



def func_1(hours, stavka, bonus):
    result = (hours * stavka) + bonus
    return result

def main():

    try:
        hours = int(argv[1])
        stavka = int(argv[2])
        bonus = int(argv[3])
    except:
        print("no ok")

    res = func_1(hours=hours, stavka=stavka, bonus=bonus)

    print(res)

if __name__ == "__main__":
    main()