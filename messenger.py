from collections import Counter


def messenger(m):
    numb_of_repeats = Counter(m)  # Count occurrences of each character
    output = [char + str(count) for char, count in numb_of_repeats.items()]
    final = "".join(output)  # Join the formatted parts into a single string
    print(final)


message = input()
messenger(message)
