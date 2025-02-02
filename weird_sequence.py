def weird_sequence(desired_number):
    final_sequence = []
    counter = 0
    while len(final_sequence) < desired_number:
        final_sequence.extend(str(10**counter))
        counter += 1
    return final_sequence[desired_number - 1]


desired_number = int(input())
print(weird_sequence(desired_number))
