def T_shirt(wanted_shirts, size):
    print(wanted_shirts, size)
    given_shirts = []
    for item in range(len(size)):
        if size[item] == "S":
            if wanted_shirts[0] > 0:
                given_shirts.append("S")
                wanted_shirts[0] -= 1
            elif size[item] == "S" and wanted_shirts[1] > 0:
                given_shirts.append("M")
                wanted_shirts[1] -= 1
            elif size[item] == "S" and wanted_shirts[2] > 0:
                given_shirts.append("L")
                wanted_shirts[2] -= 1
            else:
                given_shirts.append("No Shirt")
        elif size[item] == "M":
            if wanted_shirts[1] > 0:
                given_shirts.append("M")
                wanted_shirts[1] -= 1
            elif size[item] == "M" and wanted_shirts[2] > 0:
                given_shirts.append("L")
                wanted_shirts[2] -= 1
            elif size[item] == "M" and wanted_shirts[0] > 0:
                given_shirts.append("S")
                wanted_shirts[0] -= 1
            elif size[item] == "M" and wanted_shirts[3] > 0:
                given_shirts.append("XL")
                wanted_shirts[3] -= 1
            else:
                given_shirts.append("No Shirt")
        elif size[item] == "L":
            if wanted_shirts[2] > 0:
                given_shirts.append("L")
                wanted_shirts[2] -= 1
            elif size[item] == "L" and wanted_shirts[3] > 0:
                given_shirts.append("XL")
                wanted_shirts[3] -= 1
            elif size[item] == "L" and wanted_shirts[1] > 0:
                given_shirts.append("M")
                wanted_shirts[1] -= 1
            elif size[item] == "L" and wanted_shirts[4] > 0:
                given_shirts.append("XXL")
                wanted_shirts[4] -= 1
            elif size[item] == "L" and wanted_shirts[0] > 0:
                given_shirts.append("S")
                wanted_shirts[0] -= 1
            else:
                given_shirts.append("No Shirt")
        elif size[item] == "XL":
            if wanted_shirts[3] > 0:
                given_shirts.append("XL")
                wanted_shirts[3] -= 1
            elif size[item] == "XL" and wanted_shirts[4] > 0:
                given_shirts.append("XXL")
                wanted_shirts[4] -= 1
            elif size[item] == "XL" and wanted_shirts[2] > 0:
                given_shirts.append("L")
                wanted_shirts[2] -= 1
            elif size[item] == "XL" and wanted_shirts[1] > 0:
                given_shirts.append("M")
                wanted_shirts[1] -= 1
            else:
                given_shirts.append("No Shirt")
        elif size[item] == "XXL":
            if wanted_shirts[4] > 0:
                given_shirts.append("XXL")
                wanted_shirts[4] -= 1
            elif size[item] == "XXL" and wanted_shirts[3] > 0:
                given_shirts.append("XL")
                wanted_shirts[3] -= 1
            elif size[item] == "XXL" and wanted_shirts[2] > 0:
                given_shirts.append("L")
                wanted_shirts[2] -= 1
            else:
                given_shirts.append("No Shirt")
    print("\n".join(given_shirts))


size = []
s_m_l_xl_xxl = list(map(int, input().split()))
num_of_people = int(input())
for i in range(num_of_people):
    size.extend(input().split())
T_shirt(s_m_l_xl_xxl, size)
