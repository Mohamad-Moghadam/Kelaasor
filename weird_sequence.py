def weird_sequence(desired_number):
    final_sequence = []
    for counter in range(desired_number):
        final_sequence.extend(str(10**counter))
        if len(final_sequence) >= desired_number:
            break
    return final_sequence[desired_number - 1]


desired_number = int(input())
print(weird_sequence(desired_number))
