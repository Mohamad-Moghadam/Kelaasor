def only_once(a, b):
    final_list = list(zip(a, b))
    filtered_list = [item for item in final_list if item[0] != item[1]]
    if not filtered_list:
        return "YES"
    differences = [abs(item[0] - item[1]) for item in filtered_list]
    for i in range(len(differences) - 1):
        final_difference = differences[i] - differences[i + 1]
    if final_difference == 0:
        print("YES")
    else:
        print("NO")


first_list = list(map(int, input().split()))
second_list = list(map(int, input().split()))
only_once(first_list, second_list)
