PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt", mode="r") as letter:
    list_of_names = letter.readlines()

print(list_of_names)

with open("Input/Letters/starting_letter.txt", mode="r") as starting_letter:
    letter_content = starting_letter.read()

print(letter_content)

for names in list_of_names:
    corrected_names = names.strip("\n")
    final_letter = letter_content.replace(PLACEHOLDER, corrected_names)
    with open(f"Output/ReadyToSend/letter_for_{corrected_names}.txt", mode="w") as completed_letter:
        completed_letter.write(final_letter)
