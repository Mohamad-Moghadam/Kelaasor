def absolute(num):
    c = []
    add = 0
    absolute = 0
    maximum = 0
    for i in range(len(num)):
        for j in range(len(num[i])):
            add += num[i][j]
            absolute += abs(absolute + num[i][j])
            maximum = max(absolute, add)
            absolute = maximum
            add = maximum
        c.append(maximum)
        maximum = 0
        add = 0
        absolute = 0
    c = list(map(str, c))
    final = "\n".join(c)
    print(final)


given_numbers = []
number_of_tests = int(input())
for i in range(number_of_tests):
    given_numbers.append(list(map(int, input().split())))
absolute(given_numbers)
