def lost_person(num):
    if num[0] != 1:
        print(1)
        return
    for i in range(1, len(num)):
        if num[i] - num[i - 1] != 1:
            print(num[i - 1] + 1)
            return
    print(num[-1] + 1)


numbers = list(map(int, input().split()))
sorted_nums = sorted(numbers)
lost_person(sorted_nums)
