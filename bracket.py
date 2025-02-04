def bracket(b):
    if len(b) % 2 == 0:
        for i in range(len(b) // 2):
            if i == 0:
                if ord(b[0]) == 40 and ord(b[-1]) == 41:
                    outcome = True
                elif ord(b[0]) == 91 and ord(b[-1]) == 93:
                    outcome = True
                elif ord(b[0]) == 123 and ord(b[-1]) == 125:
                    outcome = True
                else:
                    outcome = False
            else:
                if ord(b[i]) == 40 and ord(b[(-i) - 1]) == 41:
                    outcome = True
                elif ord(b[i]) == 91 and ord(b[(-i) - 1]) == 93:
                    outcome = True
                elif ord(b[i]) == 123 and ord(b[(-i) - 1]) == 125:
                    outcome = True
                else:
                    outcome = False
    else:
        outcome = False
    print(outcome)


brackets = input().strip()
bracket(brackets)
