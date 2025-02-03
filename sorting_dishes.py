def sort(d):
    zero_list = []
    for i in range(len(d)):
        if (
            (d[i] == 0)
            and (d[i + 1] == 0 or d[i + 1] == 1)
            and (d[i - 1] == 1 or d[i - 1] == 0)
        ):
            zero_list.append(i)
    print(len(zero_list))
    # zero_list = [i for i in d if i == 0]
    # ones_list = [i for i in d if i == 1]
    # combination = len(zero_list) + len(ones_list)
    # print(combination)


the_dishes = list(map(int, input().split()))
sort(the_dishes)
