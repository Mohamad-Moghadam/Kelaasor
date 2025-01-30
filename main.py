from projects import *


def main_menu():
    while True:
        print(
            f"\nwhich set of projects do you want to check? \n1. first set of projects\n2. second set of projects\n3. third set of projects\n4. fourth set of projects\n5. fifth set of projects\n6. Exit\n"
        )
        choice = int(input("Please enter a number: "))
        if choice == 1:
            first_projects()
        elif choice == 2:
            second_projects()
        elif choice == 3:
            third_projects()
        elif choice == 4:
            fourth_projects()
        elif choice == 5:
            fifth_projects()
        elif choice == 6:
            print("Exiting the program. ")
            break


if __name__ == "__main__":
    main_menu()
