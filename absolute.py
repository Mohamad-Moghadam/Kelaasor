def absolute(num):
    c = []
    start = 0
    for i in range(len(num)):
        for j in range(len(num[i])):
            if num[i][j] >= 0:
                start += num[i][j]
                c.append(start)
                if j == num[-1]:
                    start = 0
                    break
            elif num[i][j] < 0:
                start += num[i][j]
                if start < 0:
                    start = -start
                    c.append(start)
                    if j == num[-1]:
                        start = 0
                        break
    print(start)
    print(c)


given_numbers = []
number_of_tests = int(input())
for i in range(number_of_tests):
    given_numbers.append(list(map(int, input().split())))
print(given_numbers)
absolute(given_numbers)
