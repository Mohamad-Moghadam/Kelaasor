def lost_person(num):
    if num[0] == 1:
        for i in range(len(num)):
            if i > 0 and num[i] - num[i - 1] != 1:
                print(num[i - 1] + 1)
            else:
                print(num[-1] + 1)
    else:
        print(1)


numbers = list(map(int, input().split()))
sorted_nums = sorted(numbers)
lost_person(sorted_nums)
