def get_num():
    while True:
        try:
            num = int(input("Please enter number: "))
            return num
        except ValueError:
            print("Please enter an integer [>:(]")


nums = range(1, get_num() + 1)
for num in nums:
    for i in nums:
        print(f"{i * num:4}", end=" ")
    print()
