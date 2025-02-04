def absolute(num):
    c = 0
    for i in range(len(num)):
        if num[i] >= 0:
            c += num[i]
        elif num[i] < 0:
            c += num[i]
            if c < 0:
                c = -c
    print(c)


number_of_tests = int(input())
for i in range(number_of_tests):
    given_numbers = list(map(int, input().split()))
absolute(given_numbers)
