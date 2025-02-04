def messenger(m):
    i = 0
    while i < len(m):
        c = 1
        while i + 1 < len(m) and m[i] == m[i + 1]:
            c += 1
            i += 1
        m.insert(i + 1, str(c))

    print(" ".join(m))


message = input().split()
messenger(message)
