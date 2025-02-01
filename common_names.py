from collections import Counter
from pprint import pprint


def most_common_names():
    name_list = []
    num = int(input(""))
    for count in range(num):
        name_sex = input().split()
        name_list.append(name_sex)
    male = [name for name, gender in name_list if gender == "m"]
    female = [name for name, gender in name_list if gender == "f"]
    ordered_list_m = sorted(male)
    ordered_list_f = sorted(female)
    m_counter = Counter(ordered_list_m).most_common(1)
    f_counter = Counter(ordered_list_f).most_common(1)

    most_common_males = m_counter[0] if m_counter else None
    most_common_females = f_counter[0] if f_counter else None

    pprint(most_common_males, most_common_females)


most_common_names()
