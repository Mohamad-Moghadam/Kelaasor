def weird_sequence(desired_number):
    final_sequence = ""
    n = 0
    while len(final_sequence) < desired_number:
        final_sequence += str(10**n)
        n += 1
    print(final_sequence[desired_number - 1])


desired_number = int(input())
weird_sequence(desired_number)
