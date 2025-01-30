def curse_on(the_name):
    for i in the_name:
        new_name = the_name.replace(" ", "_")
    return new_name


the_name_of_the_folder = input()
print(curse_on(the_name_of_the_folder))
