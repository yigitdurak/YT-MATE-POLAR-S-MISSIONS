def get_num():
    while True:
        try:
            num = int(input("Please enter number"))
            return num
        except ValueError:
            print("Please enter an integer")


def main():
    N = get_num()
    numbers = []
    numbers = list(range(1, N + 1))
    result = sum(numbers)
    print(f"summary is {result}")


main()
