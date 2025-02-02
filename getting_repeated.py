from collections import Counter
import pprint


def repeated(the_numbers):
    repeated_list = Counter(the_numbers)
    output = [i for i, count in repeated_list.items() if count > 1]
    return output


final_list = []
num_of_people = int(input())
for num in range(num_of_people):
    id_num = input().split()
    id_list = list(map(int, id_num))
    final_list.extend(id_num)

pprint(repeated(final_list))
