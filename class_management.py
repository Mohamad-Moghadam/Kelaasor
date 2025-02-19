class Teacher:
    def __init__(self, name):
        self.__name = name

    def change_name(self):
        self.__name = input("the new name: ")

class Student:
    def __init__(self, name, grades: list=[]):
        self.__name = name
        self.__grades = grades

    def name_change(self, new_name):
        self.__name = new_name

    def add_grade(self, new_grade : int = 0):
        self.__grades.append(new_grade)
        for i in range(len(self.__grades)):
                gpa = (sum(self.__grades[i]))/ len(self.__grades)
                print(gpa)

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
        