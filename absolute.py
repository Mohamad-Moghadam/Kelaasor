def absolute(num):
    c = []
    final = []
    start = 0
    for i in range(len(num)):
        for j in range(len(num[i])):
            if num[i][j] >= 0:
                start += num[i][j]
                c.append(start)
            elif num[i][j] < 0 and j + 1 < len(num[i]) and num[i][j + 1] < 0:
                start += num[i][j] + num[i][j + 1]
                if j + 1 > len(num[i]) or num[i][j + 1] > 0:
                    start = abs(start)
                    c.append(start)
            elif num[i][j] < 0:
                start += num[i][j]
                if start < 0:
                    start = abs(start)
                    c.append(start)
        del c[:-1]
        final.extend(c)
        start = 0
    print(final)


given_numbers = []
number_of_tests = int(input())
for i in range(number_of_tests):
    given_numbers.append(list(map(int, input().split())))
print(given_numbers)
absolute(given_numbers)
