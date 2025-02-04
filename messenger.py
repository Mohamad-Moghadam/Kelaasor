def messenger(m):
    chars = []
    c = 1
    for i in range(len(m) - 1):
        if m[i] != " ":
            if m[i] == m[i + 1]:
                c += 1
            else:
                chars.append(m[i] + str(c))
                c = 1
        else:
            chars.append(" ")
    if m[-1] != " ":
        chars.append(m[-1] + str(c))
    else:
        chars.append(" ")
    final = "".join(chars)
    print(final)


message = input()
messenger(message)
