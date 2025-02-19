class Teacher:
    def __init__(self, name):
        self.__name = name

    def change_name(self):
        self.__name = input("the new name: ")

class Student:
    def __init__(self, name, grades: list):
        self.__name = name
        self.__grades = grades

    def student_changes(self, number: int):
        if number == 1:
            print(f"self.__name")
            menu()
        elif number == 2:
            self.__name = input("the new name: ")
            menu()
        elif number == 3:
            def add_grade(new_grade : int = 0):
                self.__grades.append(new_grade)
                menu()
        elif number == 4:
            for i in range(len(self.__grades)):
                gpa = sum(self.__grades[i])
                print(gpa)
                menu()
