def only_once(a, b):
    if len(a) != len(b):
        print("NO")
        return
    differences = [b[i] - a[i] for i in range(len(a))]
    start = -1
    end = -1
    for i in range(len(differences)):
        if differences[i] != 0:
            start = i
            break
    if start == -1:
        print("YES")
        return
    for i in range(len(differences) - 1, -1, -1):
        if differences[i] != 0:
            end = i
            break
    k = differences[start]
    for i in range(start, end + 1):
        if differences[i] != k:
            print("NO")
            return

    if all(d == 0 for d in differences[:start]) and all(
        d == 0 for d in differences[end + 1 :]
    ):
        print("YES")
    else:
        print("NO")


first_list = list(map(int, input().split()))
second_list = list(map(int, input().split()))
only_once(first_list, second_list)
