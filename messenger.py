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
            i += 1
        chars.append(m[-1] + str(c))

    final = "".join(chars)
    print(chars)


message = input().split()
messenger(message)
