from __future__ import annotations


class Student:
    def __init__(self, name: str, grade: int):
        self.__name = name
        self.__grade = grade

    def compare_grade(self, other_student: Student):
        if self.__grade > other_student.__grade:
            print(f"{self.__name} has a higher grade. ")
        elif self.__grade < other_student.__grade:
            print(f"{other_student.__name} has a higher grade. ")
        else:
            print(f"{self.__name} and {other_student.__name} have the same grades. ")


name_1 = input("please enter first student's name: ")
score_1 = int(input("please enter the first student's score: "))

name_2 = input("please enter first student's name: ")
score_2 = int(input("please enter the first student's score: "))

s1 = Student(name_1, score_1)
s2 = Student(name_2, score_2)

s1.compare_grade(s2)
