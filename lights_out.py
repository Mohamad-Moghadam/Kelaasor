def lights_out(a, b, c):
    row1 = a[:]
    row2 = b[:]
    row3 = c[:]

    for i in range(3):
        if row1[i] == 1:
            if i > 0:
                row1[i - 1] = 1 - row1[i - 1]
            row1[i] = 1 - row1[i]
            if i < 2:
                row1[i + 1] = 1 - row1[i + 1]
            row2[i] = 1 - row2[i]

        if row2[i] == 1:
            if i > 0:
                row2[i - 1] = 1 - row2[i - 1]
            row2[i] = 1 - row2[i]
            if i < 2:
                row2[i + 1] = 1 - row2[i + 1]
            row1[i] = 1 - row1[i]
            row3[i] = 1 - row3[i]

        if row3[i] == 1:
            if i > 0:
                row3[i - 1] = 1 - row3[i - 1]
            row3[i] = 1 - row3[i]
            if i < 2:
                row3[i + 1] = 1 - row3[i + 1]
            row2[i] = 1 - row2[i]

    on_off_row1 = [(item % 2) for item in row1]
    on_off_row2 = [(item % 2) for item in row2]
    on_off_row3 = [(item % 2) for item in row3]


line1 = list(map(int, input().split()))
line2 = list(map(int, input().split()))
line3 = list(map(int, input().split()))
lights_out(line1, line2, line3)
