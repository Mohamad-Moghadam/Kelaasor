from collections import Counter


def sort(d):
    zero_list_beginning = []
    if d[0] == 0:
        i = 0
        while i < len(d) and d[i] == 0:
            zero_list_beginning.append(i)
            i += 1

    zero_list_middle = []
    starring_point = None
    for i in range(len(d)):
        if d[i] == 1:
            starring_point = i + 1
            break

    stopping_point = None
    for i in range(len(d) - 1, -1, -1):
        if d[i] == 1:
            stopping_point = i - 1
            break

    if starring_point is not None and stopping_point is not None:
        for i in range(starring_point, stopping_point + 1):
            if d[i] == 0:
                zero_list_middle.append(i)

    zero_list_end = []
    if d[-1] == 0:
        for i in range(len(d), -1, -1):
            if i == 0:
                zero_list_end.append(i)
            else:
                break

    z1 = len(zero_list_beginning)
    z2 = len(zero_list_middle)
    z3 = len(zero_list_end)

    zero = max(z1, z2, z3)

    ones_list = [i for i in d if i == 1]
    print(len(zero_list_beginning))
    print(len(zero_list_middle))
    print(len(zero_list_middle))
    combination = len(ones_list) + zero


the_dishes = list(map(int, input().split()))
sort(the_dishes)
