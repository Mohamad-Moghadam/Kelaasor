def only_once(a, b):
    final_list = list(zip(a, b))
    filtered_list = [item for item in final_list if item[0] != item[1]]
    if not filtered_list:
        print("YES")
        return
    differences = [abs(item[0] - item[1]) for item in filtered_list]
    if all(diff == differences[0] for diff in differences):
        print("YES")
    else:
        print("NO")


first_list = list(map(int, input().split()))
second_list = list(map(int, input().split()))
only_once(first_list, second_list)
