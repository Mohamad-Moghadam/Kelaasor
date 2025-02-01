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
    m_counter = Counter(male).most_common(1)
    f_counter = Counter(female).most_common(1)

    most_common_males = m_counter[0] if m_counter else None
    most_common_females = f_counter[0] if f_counter else None

    print(most_common_males, most_common_females)


most_common_names()
