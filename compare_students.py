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
            print(f"{self.__name} and {other_student.__name} has the same grades. ")


s1 = Student("Alice", 90)
s2 = Student("Bob", 91)
s1.compare_grade(s2)  # Alice has a higher grade.
