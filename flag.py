def solution_num(number):
    if number == 1 or number == 2:
        return 2
    if number % 3 == 0:
        return solution_num(number - 1) * 2
    else:
        return solution_num(number - 1) + 2


number_of_walls = int(input())
print(solution_num(number_of_walls))
