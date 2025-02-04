def bracket(b):
    for i in range(len(b)):
        if i == 0:
            if b[0] == b[-1]:
                print(True)
            else:
                print(False)


brackets = input().split()
bracket(brackets)
