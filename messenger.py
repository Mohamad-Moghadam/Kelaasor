def messenger(m):
    seen = {}
    output = []

    for char in m:
        if char != " ":
            if char not in seen:
                seen[char] = 1
            else:
                seen[char] += 1
            output.append(f"{char}{seen[char]}")
        else:
            output.append(" ")

    final = "".join(output)
    print(final)


message = input()
messenger(message)
