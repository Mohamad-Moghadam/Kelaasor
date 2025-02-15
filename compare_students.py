class Student:
    def __init__(self, name, grade):
        self.__name = name
        self.__grade = grade

    def compare_grade(self, other_student):
        if self.__grade > Student(other_student).__grade:
            return f"{self.__name} has a higher grade. "
        elif self.__grade < Student(other_student).__grade:
            return f"{Student(other_student).__name} has a higher grade. "
        else:
            return f"{self.__name} and {Student(other_student).__name} has the same grades. "
