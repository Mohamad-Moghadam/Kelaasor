from main import *
from random import randint


def first_projects():
    print(f"\nHi, Welcome to the first project!")
    name = input("What's your name? ")
    birth_year = int(input("When were you born? "))
    age = 1403 - birth_year
    print(f"{name} You have been living for {age} years.")

    while True:
        print(
            "Please enter the two numbers you want to add to each other and get the average of. "
        )
        first_num = int(input("What's the first number? "))
        second_num = int(input("What's the second number? "))
        sum = first_num + second_num
        average = sum / 2
        remaining = first_num % second_num
        quotient = int(first_num // second_num)
        print(
            f"the sum of your numbers is : {sum} and the average is : {average}, the remaining is {remaining}, and the quotient is {quotient}."
        )
        break


def second_projects():

    def age_function():
        date_of_birth = int(input("Which year were you born? "))
        if 1000 < date_of_birth < 1403:
            if 1400 < date_of_birth <= 1403:
                print("Get out of here kid! ")
            elif 1392 <= date_of_birth <= 1400:
                greetings = input("How are you kid?").capitalize
                if (
                    greetings == "GOOD"
                    or "FINE"
                    or "OK"
                    or "PERFECT"
                    or "COULDN'T BE BETTER"
                ):
                    print("that's great")
                elif (
                    greetings == "NOT BAD"
                    or "SO SO"
                    or "NOT GREAT"
                    or "COULD BE BETTER"
                    or "NOT GOOD"
                ):
                    print("Sorry to here that kiddo!")
                elif greetings == "BAD" or "REALLY BAD" or "AWFUL":
                    print("life could sometimes get tough kid! keep it up!")
                else:
                    print("OK")
            elif 1384 <= date_of_birth < 1392:
                print("Enjoying those ages, huh? ")
            elif date_of_birth > 1384:
                print("Sorry to inform you that you may die in the near future! ")
            else:
                print("what does that even mean bro? ")
        elif 1800 < date_of_birth < 2025:
            if 2022 < date_of_birth <= 2025:
                print("Get out of here kid! ")
            elif 2014 <= date_of_birth <= 2022:
                greetings = input("How are you kid?").capitalize
                if (
                    greetings == "GOOD"
                    or "FINE"
                    or "OK"
                    or "PERFECT"
                    or "COULDN'T BE BETTER"
                ):
                    print("that's great")
                elif (
                    greetings == "NOT BAD"
                    or "SO SO"
                    or "NOT GREAT"
                    or "COULD BE BETTER"
                    or "NOT GOOD"
                ):
                    print("Sorry to here that kiddo!")
                elif greetings == "BAD" or "REALLY BAD" or "AWFUL":
                    print("life could sometimes get tough kid! keep it up!")
                else:
                    print("OK")
            elif 2005 <= date_of_birth < 2014:
                print("Enjoying those ages, huh? ")
            elif date_of_birth > 2005:
                print("Sorry to inform you that you may die in the near future! ")
            else:
                print("what does that even mean bro? ")

    def bigger_num_2():
        first_number = input("what's your first number? ")
        second_number = input("what's your second number? ")
        m = max(first_number, second_number)
        print(f"the biggest number is: {m}")

    def devisable_by_7():
        the_number = int(input("what's your number? "))
        if the_number % 7 == 0:
            print("it is devisable by 7")
        else:
            print("it's not devisable by 7")

    def devisable_by_2_and_3():
        the_num = int(input("what is the number you want to check? "))
        if the_num % 2 == 0 and the_num % 3 == 0 and the_num % 5 != 0:
            print("that is valid! ")
        else:
            print("that is not valid! ")

    def devisable_by_2_or_3():
        the_num = int(input("what is the number you want to check? "))
        if (the_num % 2 == 0 or the_num % 3 == 0) and the_num % 5 != 0:
            print("that is valid! ")
        else:
            print("that is not valid! ")

    def three_num_max():
        x = int(input("first number: "))
        y = int(input("second number: "))
        z = int(input("third number: "))
        m = max(x, y, z)
        print(f"the biggest number is {m}")

    def menu():
        while True:
            print(
                f"\nwhat do u wanna do? \n1. check the age project \n2. check the bigger number out of two numbers project \n3. check if the number is devisable by 7 \n4. devisable by 2 and 3 and not by 5 \n5. devisable by 2 or 3 and not by 5 \n6. the biggest number out of three numbers\n7. Return to main menu\n"
            )
            choice = int(input("chose your choice: "))
            if choice == 1:
                age_function()
            elif choice == 2:
                bigger_num_2()
            elif choice == 3:
                devisable_by_7()
            elif choice == 4:
                devisable_by_2_and_3()
            elif choice == 5:
                devisable_by_2_or_3()
            elif choice == 6:
                three_num_max()
            elif choice == 7:
                return ()

    menu()


def third_projects():
    def hop():
        the_number = int(input("What is the desired number? "))
        for i in range(1, 101):
            if i % the_number == 0:
                print("Hop")
            else:
                print(i)

    def divisors():
        the_number = int(input("What is the desired number? "))
        for i in range(1, the_number + 1):
            if the_number % i == 0:
                print(i)

    def filled_square():
        squares = int(input("How many sides do you want your square to have? "))
        for i in range(0, squares):
            for j in range(0, squares):
                print("* ", end="")
            print()

    def empty_squares():
        squares = int(input("How many sides do you want your square to have? "))
        for i in range(0, squares):
            if i == 0 or i == squares - 1:
                print("* " * squares)
            else:
                print("* " + "  " * (squares - 2) + "* ")

    def prime_number():
        get_the_number = int(input("What is the number you want to check? "))
        if get_the_number < 2:
            print("it's not a prime number")
            return
        for i in range(2, int(get_the_number)):
            if get_the_number % i == 0:
                print("It's not a prime number")
                return
        print("It's a prime number")

    def permutation():
        print("our word is: python")
        number_of_letters = len("python")
        result = 1
        for i in range(number_of_letters, 0, -1):
            result *= i
        print(result)

    def permutation_general():
        the_word = input("what is your word? ")
        length = len(the_word)
        result = 1
        for i in range(length, 0, -1):
            result *= i
        print(f"the number of permutations of {the_word} is {result} ")

    def menu():
        while True:
            print(
                f"\nwhat do you want to do? \n1. Play Hop \n2. giving the divisors of a number\n3. drawing a filled square\n4. drawing an empty square\n5. finding out if a number is prime\n6. tell all the possible ways to write a word with the letters of (python)\n7. tell all the possible ways of writing a word with the letters of a specific word\n8. Return to main menu\n"
            )
            choice = int(input("chose your choice: "))
            if choice == 1:
                hop()
            elif choice == 2:
                divisors()
            elif choice == 3:
                filled_square()
            elif choice == 4:
                empty_squares()
            elif choice == 5:
                prime_number()
            elif choice == 6:
                permutation()
            elif choice == 7:
                permutation_general()
            elif choice == 8:
                return ()

    menu()


def fourth_projects():

    def adding_numbers():
        x = int(input("Please enter a number (0 to exit): "))
        sum = x
        while x != 0:
            x = int(input("Please enter another number (0 to exit): "))
            sum += x
            print(f"The sum of the numbers is: {sum}")
        if x == 0:
            print(
                f"You've entered 0.\nthe sum of the numbers is{sum}\n Exiting the program."
            )

    def Greatest_Common_Divisor():
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        first_number = int(input("first number: "))
        second_number = int(input("second number: "))
        result = gcd(first_number, second_number)
        print(
            f"the greatest common divisor of {first_number} and {second_number} is equal to: {result}"
        )

    def kelaasor():
        while True:
            the_input = input(
                "Please enter (kelaasor) to return to main menu: "
            ).capitalize()
            if the_input == "Kelaasor":
                print("Returning to main menu...")
                return ()

    def random_number():
        random_number = randint(0, 1000)
        guess = int(input("what do you think is the number? "))
        while guess != random_number:
            if random_number > guess:
                guess = int(input("The number is higher. Try again!"))
            elif random_number < guess:
                guess = int(input("The number is lower. Try again!"))
        print(f"that's it. the number is {random_number}")

    def Collatz_Conjecture():
        a_number = int(input("please enter your number"))
        while a_number != 1:
            if a_number % 2 == 0:
                a_number = a_number // 2
                print(a_number)
            elif a_number % 2 == 1:
                a_number = (a_number * 3) + 1
                print(a_number)
        print(f"That's it! we turned your number to 1 using the Collatz Conjecture.")

    def menu():
        while True:
            print(
                f"\nwhat do you want to do? \n1. adding numbers \n2. Greatest Common Divisor \n3. write kelaasor \n4. find the number game \n5. Collatz Conjecture \n6. Return to main menu\n"
            )
            choice = int(input("chose your choice: "))
            if choice == 1:
                adding_numbers()
            elif choice == 2:
                Greatest_Common_Divisor()
            elif choice == 3:
                kelaasor()
            elif choice == 4:
                random_number()
            elif choice == 5:
                Collatz_Conjecture()
            elif choice == 6:
                return ()

    menu()


def fifth_projects():

    def factorial():
        the_result = 1
        n = int(input("What is the desired number? "))
        for i in range(n, 1, -1):
            the_result *= i
        print(f"{the_result} is the result. ")

    def the_numbers_in_between():
        first_number = int(input("What is the lower desired number? "))
        second_number = int(input("What is the higher desired number? "))
        for i in range(first_number + 1, second_number):
            print(f"{i}")
