def absolute(num):
    c = []
    start = 0
    for i in range(len(num) - 1):
        for j in range(len(num[i])):
            if num[i][j] >= 0:
                start += num[i][j]
                c.append(start)
            elif num[i][j] < 0 and num[i][j + 1] < 0:
                num[i][j] += num[i][j + 1]
                start += num[i][j]
                if start < 0:
                    start = -start
                    c.append(start)
            elif num[i][j] < 0:
                start += num[i][j]
                if start < 0:
                    start = -start
                    c.append(start)
        start = 0
    print(start)
    print(c)


given_numbers = []
number_of_tests = int(input())
for i in range(number_of_tests):
    given_numbers.append(list(map(int, input().split())))
print(given_numbers)
absolute(given_numbers)
