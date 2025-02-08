def max_c_value(case):

    results = []
    if 2 ** len(case) == len(results):
        return max(results)

    c1 = 0
    c2 = 0
    for i in range(len(case)):
        c1 += case[i]
        c2 = abs(c2 + case[i])
        results.append(c1)
        results.append(c2)
        if 2**i != len(case):
            del results[: (2**i) + 1]
    print(results)


num_list = int(input())
num_list_final = []
for i in range(num_list):
    a = list(map(int, input().split()))
    result = max_c_value(a)
    del num_list_final[:]
