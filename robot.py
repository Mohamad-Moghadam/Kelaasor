import sys


class Robot:
    def __init__(self, m: int, n: int, i: int, j: int):
        self.__sheet = [m, n]
        self.__placement_horizontal = i
        self.__placement_vertical = j

    def move_up(self):
        if self.__placement_vertical < self.__sheet[1]:
            self.__placement_vertical += 1
        else:
            print(f"The robot can't get any higher. ")
            self.__str__()

    def move_left(self):
        if self.__placement_horizontal > 1:
            self.__placement_horizontal -= 1
        else:
            print(f"The robot can't get to the left. ")
            self.__str__()

    def move_down(self):
        if self.__placement_vertical > 1:
            self.__placement_vertical -= 1
        else:
            print(f"The robot can't get any lower. ")
            self.__str__()

    def move_right(self):
        if self.__placement_horizontal < self.__sheet[0]:
            self.__placement_horizontal += 1
        else:
            print(f"The robot can't get any higher. ")
            self.__str__()

    def __str__(self):
        return (
            f"last location: {self.__placement_horizontal}, {self.__placement_vertical}"
        )


r = Robot(5, 5, 2, 2)
r.move_up()
r.move_left()
r.move_down()
r.move_right()
r.move_up()
print(r)
