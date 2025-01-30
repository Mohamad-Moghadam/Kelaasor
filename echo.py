def echo_effect(word):
    final = []
    length = len(word)

    for i in range(length):
        until_first_part = word[:i]
        first_part = word[i] * i
        new_words = word.replace(until_first_part, first_part)
        final.append(new_words)
    return final


input_word = input()
print(*echo_effect(input_word), sep="\n")
