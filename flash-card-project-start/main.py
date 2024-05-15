import os
import random
from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

# import data as a dictionary
path = 'data/words_to_learn.csv'
check_file = os.path.isfile(path)

if check_file:
    dataframe = pd.read_csv('data/words_to_learn.csv')
else:
    dataframe = pd.read_csv('data/french_words.csv')

words_to_learn = dataframe.to_dict(orient="records")
random_word = {}


# -----------------------------------------  Change Back  -------------------------------------------------

def change_back():
    new_en_word = random_word["English"]

    canvas.itemconfig(canvas_side, image=back_image)
    canvas.itemconfig(title_word, text="English", fill="white")
    canvas.itemconfig(meaning_word, text=new_en_word, fill="white")


# -----------------------------------------  NEW WORD  -------------------------------------------------

def new_word():
    global change_time, random_word

    window.after_cancel(change_time)

    random_word = random.choice(words_to_learn)

    new_fr_word = random_word["French"]

    canvas.itemconfig(canvas_side, image=front_image)
    canvas.itemconfig(title_word, text="French", fill="black")
    canvas.itemconfig(meaning_word, text=new_fr_word, fill="black")

    change_time = window.after(3000, func=change_back)


# -----------------------------------------  Remove Word  -------------------------------------------------

def correct_button_func():
    words_to_learn.remove(random_word)
    updated_word_final = pd.DataFrame.from_dict(words_to_learn)

    updated_word_final.to_csv('data/words_to_learn.csv', index=False)

    change_back()
    new_word()


# -----------------------------------------  UI SETUP  -------------------------------------------------

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

change_time = window.after(3000, func=change_back)

# Images import

canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)

front_image = PhotoImage(file='images/card_front.png')
back_image = PhotoImage(file='images/card_back.png')

canvas_side = canvas.create_image(400, 263, image=front_image)

title_word = canvas.create_text(400, 150, text="Title", font=('Arial', 40, 'italic'), fill="black")
meaning_word = canvas.create_text(400, 310, text="Word", font=('Arial', 60, 'bold'), fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# Right and Wrong Buttons

image_right = PhotoImage(file='images/right.png')
button_right = Button(image=image_right, highlightthickness=0, borderwidth=0, command=correct_button_func)
button_right.grid(column=1, row=1)

image_wrong = PhotoImage(file='images/wrong.png')
button_wrong = Button(image=image_wrong, highlightthickness=0, borderwidth=0, command=new_word)
button_wrong.grid(column=0, row=1)

new_word()

window.mainloop()
