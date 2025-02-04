def T_shirt(wanted_shirts, size):
    given_shirts = []
    for item in size:
        if item == "S" and wanted_shirts[0] > 0:
            given_shirts.append("S")
            wanted_shirts[0] -= 1
        elif item == "S" and wanted_shirts[1] > 0:
            given_shirts.append("M")
            wanted_shirts[1] -= 1
        elif item == "S" and wanted_shirts[2] > 0:
            given_shirts.append("L")
            wanted_shirts[2] -= 1
        else:
            given_shirts.append("No Shirt")
        if item == "M" and wanted_shirts[1] > 0:
            given_shirts.append("M")
            wanted_shirts[1] -= 1
        elif item == "M" and wanted_shirts[2] > 0:
            given_shirts.append("L")
            wanted_shirts[2] -= 1
        elif item == "M" and wanted_shirts[0] > 0:
            given_shirts.append("S")
            wanted_shirts[0] -= 1
        elif item == "M" and wanted_shirts[3] > 0:
            given_shirts.append("XL")
            wanted_shirts[3] -= 1
        else:
            given_shirts.append("No Shirt")
        if item == "L" and wanted_shirts[2] > 0:
            given_shirts.append("L")
            wanted_shirts[2] -= 1
        elif item == "L" and wanted_shirts[3] > 0:
            given_shirts.append("XL")
            wanted_shirts[3] -= 1
        elif item == "L" and wanted_shirts[1] > 0:
            given_shirts.append("M")
            wanted_shirts[1] -= 1
        elif item == "L" and wanted_shirts[4] > 0:
            given_shirts.append("XXL")
            wanted_shirts[4] -= 1
        elif item == "L" and wanted_shirts[0] > 0:
            given_shirts.append("S")
            wanted_shirts[0] -= 1
        else:
            given_shirts.append("No Shirt")
        if item == "XXL" and wanted_shirts[4] > 0:
            given_shirts.append("XXL")
            wanted_shirts[4] -= 1
        elif item == "XXL" and wanted_shirts[3] > 0:
            given_shirts.append("XL")
            wanted_shirts[3] -= 1
        elif item == "XXL" and wanted_shirts[2] > 0:
            given_shirts.append("L")
            wanted_shirts[2] -= 1
        else:
            given_shirts.append("No Shirt")
    return


size = []
s_m_l_xl_xxl = input().split()
num_of_people = int(input())
for i in range(num_of_people):
    size.append(input().split())
T_shirt(s_m_l_xl_xxl, size)
