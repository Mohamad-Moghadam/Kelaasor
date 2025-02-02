from collections import Counter


def recognize(name):
    name = name.replace(" ", "")
    final = []
    number_of_index = Counter(name)
    for key, value in number_of_index.items():
        if value == 1:
            final.append(key)
    if len(final) % 2 == 0:
        print("Human")
    else:
        print("Alien")


entered_name = input()
recognize(entered_name)
