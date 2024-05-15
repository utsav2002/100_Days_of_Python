import pandas as pd

data_frame = pd.read_csv('nato_phonetic_alphabet.csv')

# # update the dictionary
# for (index, row) in data_frame.iterrows():
#     row_letter = row.letter
#     row_code = row.code
#     phonetic_dict.update({row_letter:row_code for (row.letter, row.code) in data_frame.iterrows()})

# another method
phonetic_dict = {
    row.letter:row.code for (index, row) in data_frame.iterrows()
}

user_name = ""
result = []
# User-name input
def full_func():
    user_name = (input("What is your name?: ").upper()).replace(" ", "")
    try:
        result = [phonetic_dict[letter] for letter in user_name]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        full_func()
    else:
        print(result)

full_func()