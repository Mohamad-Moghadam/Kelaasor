import copy


def lights_out(a, b, c):

    for i in range(3):
        if a[i] % 2 == 1 and b[i] % 2 == 1 and c[i] % 2 == 1:
            print("0 0 0")
            print("0 0 0")
            print("0 0 0")
            return

    row1 = copy.deepcopy(a)
    row2 = copy.deepcopy(b)
    row3 = copy.deepcopy(c)

    if a[0] > 0:
        row1[1] += a[0]
        row2[0] += a[0]
    if a[1] > 0:
        row1[0] += a[1]
        row1[2] += a[1]
    if a[2] > 0:
        row1[1] += a[2]
        row2[2] += a[2]
    if b[0] > 0:
        row1[0] += b[0]
        row2[1] += b[0]
        row3[0] += b[0]
    if b[1] > 0:
        row2[0] += b[1]
        row1[1] += b[1]
        row3[1] += b[1]
        row2[2] += b[1]
    if b[2] > 0:
        row2[1] += b[2]
        row1[2] += b[2]
        row3[2] += b[2]
    if c[0] > 0:
        row2[0] += c[0]
        row3[1] += c[0]
    if c[1] > 0:
        row3[0] += c[1]
        row2[1] += c[1]
        row3[2] += c[1]
    if c[2] > 0:
        row3[1] += c[2]
        row2[2] += c[2]

    on_off_row1 = list(map(str, [((item + 1) % 2) for item in row1]))
    on_off_row2 = list(map(str, [((item + 1) % 2) for item in row2]))
    on_off_row3 = list(map(str, [((item + 1) % 2) for item in row3]))

    print(" ".join(on_off_row1))
    print(" ".join(on_off_row2))
    print(" ".join(on_off_row3))


line1 = list(map(int, input().split()))
line2 = list(map(int, input().split()))
line3 = list(map(int, input().split()))

lights_out(line1, line2, line3)
