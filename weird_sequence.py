def weird_sequence(desired_number):
    sequence = [10**n for n in range(desired_number)]
    final_sequence = "".join(map(str, sequence))
    the_number = final_sequence[desired_number - 1]
    print(the_number)


desired_number = int(input())
weird_sequence(desired_number)
