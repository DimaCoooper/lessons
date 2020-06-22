
def new_func():
    list = [i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0]
    return(list)

def main():
    print(new_func())

if __name__ == "__main__":
    main()
