class Teacher:
    def __init__(self, name):
        self.__name = name

    def change_name(self):
        self.__name = input("the new name: ")