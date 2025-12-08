import time


def get_num():
    while True:
        try:
            num = int(input("Please enter number"))
            return num
        except ValueError:
            print("Please enter an integer")


def main():
    nums = get_num()
    for num in range(nums, 0, -1):
        print(f"\r\033[K{num}", end="\r")
        time.sleep(1)
    print("booooooooooooooooooooooooooooooooooooooooooom")


main()
