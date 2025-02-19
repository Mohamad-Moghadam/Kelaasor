class Teacher:
    def __init__(self, name):
        self.__name = name

    def change_name(self):
        self.__name = input("the new name: ")

class Student:
    def __init__(self, name, grades: list=[]):
        self.__name = name
        self.__grades = grades

    def student_changes(self, number: int):
        if number == 1:
            print(f"self.__name")
            s_menu()
        elif number == 2:
            self.__name = input("the new name: ")
            s_menu()
        elif number == 3:
            def add_grade(new_grade : int = 0):
                self.__grades.append(new_grade)
                s_menu()
        elif number == 4:
            for i in range(len(self.__grades)):
                gpa = sum(self.__grades[i])
                print(gpa)
                s_menu()




class Lesson:
    def __init__(self, teacher: Teacher, students: list):
        self.__teacher = teacher
        self.__students = students

    def change_teacher(self):
        name = input("the new teacher: ")
        self.__teacher = Teacher(name)

    def add_student(self):
        name = input("new student: ")
        self.__students.append(Student(name))

    def grade(self):
        