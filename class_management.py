class Teacher:
    def __init__(self, name):
        self.__teacher_name = name

    def change_name(self, new_name):
        self.__teacher_name = new_name

class Student:
    def __init__(self, name, grades: list=[]):
        self.__student_name = name
        self.__grades = grades

    def name_change(self, new_name):
        self.__student_name = new_name

    def add_grade(self, new_grade : float):
        self.__grades.append(new_grade)
        gpa = (sum(self.__grades))/len(self.__grades)
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
        for person in self.__students:
            listed_grades = input()
            grades_list.extend(listed_grades)
            person.add_grade(listed_grades)
        zipped = zip(self.__students, grades_list)
        return zipped

    def show_list(self, zipped):
        for i in self.__students:
            print(f"{i}, {zipped}")


t1 = Teacher("Mr.ghodoosi")
t2 = Teacher("Mr.goldoost")
s1 = Student("Mr.Abedini")
s2 = Student("Mohamad Hossain")
l1 = Lesson(t1, s1)

t1.change_name("Mr.kani")

s1.name_change("Ms.abedini")

s1.add_grade(10)
s1.add_grade(15)
s1.add_grade(20)

l1.change_teacher(t2)
l1.add_student(s2)
