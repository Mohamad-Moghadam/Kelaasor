def weird_sequence(desired_number):
    final_sequence = ""
    counter = 0
    while len(final_sequence) < desired_number:
        final_sequence += str(10**counter)
        counter += 1
    print(final_sequence[desired_number - 1])


desired_number = int(input())
weird_sequence(desired_number)
