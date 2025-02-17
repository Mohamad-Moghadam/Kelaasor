class Person:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.age = age

    def birthday(self):
        self.age += 1

    def __str__(self):
        return f"{self.age}"


name = input("please enter your name: ")
age = int(input("please enter your age: "))

p = Person(name, age)
p.birthday()
print(p)
