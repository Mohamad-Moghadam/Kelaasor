def weird_sequence(n):
    i = int(((1 + (1 + 8 * (n - 1)) ** 0.5) / 2))
    if (i * (i - 1)) // 2 == (n - 1):
        return 1
    else:
        return 0


desired_number = int(input())
print(weird_sequence(desired_number))
