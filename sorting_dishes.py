from collections import Counter


def sort(d):
    zero_list_beginning = []
    if d[0] == 0:
        i = 0
        while i < len(d) and d[i] == 0:
            zero_list_beginning.append(i)
            i += 1

    first_one = None
    for i in range(len(d)):
        if d[i] == 1:
            first_one = i
            break

    last_one = None
    for i in range(len(d) - 1, -1, -1):
        if d[i] == 1:
            last_one = i
            break

    max_zero_sequence = 0
    current_zeros = 0
    for i in range(first_one, last_one + 1):
        if d[i] == 0:
            current_zeros += 1
        else:
            zero_list_middle = max(max_zero_sequence, current_zeros)
            current_zeros = 0

    zero_list_end = []
    if d[-1] == 0:
        for i in range(len(d) - 1, -1, -1):
            if d[i] == 0:
                zero_list_end.append(i)
            else:
                break

    z1 = len(zero_list_beginning)
    z2 = zero_list_middle
    z3 = len(zero_list_end)

    zero = max(z1, z2, z3)

    ones_list = [i for i in d if i == 1]
    combination = len(ones_list) + zero
    print(zero_list_middle)
    print(combination)


the_dishes = list(map(int, input().split()))
sort(the_dishes)
