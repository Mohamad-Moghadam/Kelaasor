from itertools import chain


def encryption(inserted_number, inserted_text):
    return "".join(
        (
            chr(((ord(c) - 65 + inserted_number) % 26) + 65)
            if "A" <= c <= "Z"
            else (
                chr(((ord(c) - 97 + inserted_number) % 26) + 97)
                if "a" <= c <= "z"
                else c
            )
        )
        for c in inserted_text
    )


num = int(input())
text = input()
print(encryption(num, text))
