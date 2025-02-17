import hashlib
import sys


class User:
    def __init__(self, username, password):
        self.__users = {}
        self.__name = username
        self.__password = password
        self.__users[self.__name] = self.__password

    def hash_name(self):
        name_bytes = self.__name.encode("utf-8")
        self.__password = self.__hashed_name = hashlib.sha256(name_bytes).hexdigest()

    def authenticate(self, given_name, given_password):
        if self.__users[self.__name] == self.__password.hash_name():
            print(f"identity confirmed✅ ")
        else:
            print(f"wrong! ")
            sys.exit()


user_list = []
user_list.append(User("Faezeh", "123456"))
user_list.append(User("Fariborz", "ffborz"))
user_list.append(User("Hamed", "kelaasor"))

for user in user_list:
    print(user.authenticate("Mohammad", "123456"))  # prints 3 False

for user in user_list:
    print(user.authenticate("Fariborz", "ffborz"))  # prints False, True, False
