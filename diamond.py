def draw_double_diamond(the_number):

    for i in range(the_number // 2 + 1):
        space = the_number // 2 - i
        double_space = the_number - (2 * i + 1)
        stars = 2 * i + 1
        print(f"{space * " "}{"*" * stars}{double_space * " "}{stars * "*"}")

    for j in range(1, the_number):
        decreasing_space = j
        in_between_decreasing_space = 2 * (decreasing_space)
        decreasing_stars = the_number - (j * 2)
        print(
            f"{" " * decreasing_space}{'*' * decreasing_stars}{' ' * in_between_decreasing_space}{'*' * decreasing_stars}"
        )


entered_number = int(input("please enter a number: "))
draw_double_diamond(entered_number)
