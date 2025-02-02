def lights_out(a, b, c):

    added1 = [(index + 1) % 2 for index in a if index > 0]
    added2 = [(index + 1) % 2 for index in b if index > 0]
    added3 = [(index + 1) % 2 for index in c if index > 0]


line1 = list(map(int, input().split()))
line2 = list(map(int, input().split()))
line3 = list(map(int, input().split()))
lights_out(line1, line2, line3)
