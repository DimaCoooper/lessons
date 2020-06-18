def numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'No / 0'
    except ValueError:
        return 'No value'


def main():
    a = int(input("введите число 1: "))
    b = int(input("введите число 2: "))
    v = numbers(a, b)
    print(v)

main()

