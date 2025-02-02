def encryption(inserted_number, inserted_text):
    new_text = [chr(ord(char) + inserted_number) for char in inserted_text]
    final_text = "".join(new_text)
    return final_text


num = int(input())
text = input()
print(encryption(num, text))
