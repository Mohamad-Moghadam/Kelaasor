def bracket(b):
    for i in range(len(b)):
        if i == 0:
            if ord(b[0]) == 40:
                if ord(b[-1]) == 41:
                    print(True)
            elif ord(b[0]) == 91:
                if ord(b[-1]) == 93:
                    print(True)
            elif ord(b[0]) == 123:
                if ord(b[-1]) == 125:
                    print(True)
            else:
                print(False)


brackets = input()
new_brackets = " ".join(brackets)
bracket_list = new_brackets.split()
print(bracket_list)
bracket(bracket_list)
