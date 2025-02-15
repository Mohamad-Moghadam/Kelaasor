class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def birthday(self):
        self.__age += self.__age

    def __str__(self):
        return f"{self.__age.birthday()}"


p = Person("Alice", 25)
p.birthday()
print(p.age)  # output: 26
