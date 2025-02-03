from collections import Counter


def messenger(m):
    numb_of_repeats = Counter(m)
    output = [
        char + str(count) if char != " " else " "
        for char, count in numb_of_repeats.items()
    ]
    final = "".join(output)
    print(final)


message = input()
messenger(message)
