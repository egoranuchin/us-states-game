#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend"

PLACEHOLER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()


with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
        # letter = starting_letter.replace("[name]", name)
    # broken = list(letter)
    # print(broken)