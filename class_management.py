class Teacher:
    def __init__(self, name):
        self.__teacher_name = name

    def change_name(self):
        self.__teacher_name = input("the new name: ")

class Student:
    def __init__(self, name, grades: list=[]):
        self.__student_name = name
        self.__grades = grades

    def name_change(self, new_name):
        self.__student_name = new_name

    def add_grade(self, new_grade : int = 0):
        self.__grades.append(new_grade)
        for i in range(len(self.__grades)):
                gpa = (sum(self.__grades[i]))/ len(self.__grades)
                print(gpa)

class Lesson:
    def __init__(self, teacher: Teacher, students: list):
        self.__teacher = teacher
        self.__students = students

    def change_teacher(self, new_teacher : Teacher):
        self.__teacher = new_teacher

    def add_student(self, new_student: Student):
        self.__students.append(new_student)

    def grade(self):
        grades_list = []
        print(self.__students)
        for person in self.__students:
            listed_grades = input()
            grades_list.extend(listed_grades)
            person.add_grade(listed_grades)
        return zipped = zip(self.__students, grades_list)

    def show_list(self, zipped):
        for i in self.__students:
            print(f"{i}, {zipped}")