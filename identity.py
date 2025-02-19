import hashlib
import sys


class User:
    def __init__(self, username, password):
        self.__name = username
        self.__password = self.hash_password(password)

    def hash_password(self, given_password):
        return hashlib.sha256(given_password.encode()).hexdigest()

    def authenticate(self, given_name, given_password):
        return self.__name == given_name and self.__password == self.hash_password(given_password)

user_list = []
user_list.append(User("Faezeh", "123456"))
user_list.append(User("Fariborz", "ffborz"))
user_list.append(User("Hamed", "kelaasor"))

for user in user_list:
    print(user.authenticate("Mohammad", "123456"))  # prints 3 False

for user in user_list:
    print(user.authenticate("Fariborz", "ffborz"))  # prints False, True, False
