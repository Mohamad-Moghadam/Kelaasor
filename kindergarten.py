def kindergarten(kids):
    kids = list(kids)
    i = 0
    while i < len(kids) - 1:
        if kids[i] == "B" and kids[i + 1] == "G":
            kids[i], kids[i + 1] = kids[i + 1], kids[i]
            i += 1
        i += 1
    return "".join(kids)


number_of_kids = list(map(int, input().split()))
moments = number_of_kids[1]
order = input().strip()

for _ in range(moments):
    order = kindergarten(order)

print(order)
