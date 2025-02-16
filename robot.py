class Robot:
    def __init__(self, m: int, n: int, i: int, j: int):
        self.__sheet = [m, n]
        self.__placement_horizontal = i
        self.__placement_vertical = j

    def move_up(self):
        if self.__placement_vertical < self.__sheet[1]:
            self.__placement_vertical += 1
        else:
            return f"The robot can't get any higher. "

    def move_left(self):
        if self.__placement_horizontal > 1:
            self.__placement_horizontal -= 1
        else:
            return f"The robot can't get to the left. "

    def move_down(self):
        if self.__placement_vertical > 1:
            self.__placement_vertical -= 1
        else:
            return f"The robot can't get any lower. "

    def move_right(self):
        if self.__placement_horizontal < self.__sheet[0]:
            self.__placement_horizontal += 1
        else:
            return f"The robot can't get any higher. "

    def __str__(self):
        return f"{self.__placement_horizontal}, {self.__placement_vertical}"


r = Robot(5, 5, 1, 1)
r.move_up()
r.move_left()
r.move_left()
print(r)
