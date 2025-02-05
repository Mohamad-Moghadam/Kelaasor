def solution_num(number):
    if number == 0:
        return 0
    elif number == 1 or number == 2:
        return 2
    else:
        return solution_num(number - 1) + 2


number_of_walls = int(input())
print(solution_num(number_of_walls))
