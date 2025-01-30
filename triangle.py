def triangle(size):
    for i in range(1, size + 1):
        print(" " * (size - i) + "*" * (2 * i - 1), end="")
        print()


desired_number = int(input("enter the number you want: "))
triangle(desired_number)
