def only_once(a, b):
    final_list = list(zip(a, b))
    filtered_list = [item for item in final_list if item[0] != item[1]]
    for i in range(len(filtered_list) - 1):
        difference = abs(filtered_list[i][0] - filtered_list[i][1])
        next_difference = abs(filtered_list[i + 1][0] - filtered_list[i + 1][1])
        if next_difference == difference + 1:
            return "Yes"
        else:
            return "No"


first_list = list(map(int, input("")))
second_list = list(map(int, input("")))
print(only_once(first_list, second_list))
