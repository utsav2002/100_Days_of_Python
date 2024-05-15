from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

WHITE = "FFFFFF"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = [choice(letters) for _ in range(randint(8, 10))]
    nr_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    nr_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = nr_letters + nr_symbols + nr_numbers
    shuffle(password_list)
    password = "".join(password_list)

    password_box.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website_entered = website_box.get()
    email_entered = email_box.get()
    password_entered = password_box.get()

    new_data = {
        website_entered.title(): {
            "email": email_entered,
            "password": password_entered
        }
    }

    if len(website_entered) == 0 or len(email_entered) == 0 or len(password_entered) == 0:
        messagebox.showinfo(title="Oops", message="Please do not leave any field empty!")

    else:
        try:
            # Try reading the data from file
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            # Create new file and write the data
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # Hold new data
            data.update(new_data)

            # Write new data i.e. updating finally
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            # data_file.write(f"{website_entered}  | {email_entered}  | {password_entered} \n")
            website_box.delete(0, END)
            email_box.delete(0, END)
            password_box.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website_to_search = (website_box.get()).title()

    try:
        with open('data.json') as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No Data File Found")

    else:
        if website_to_search in data:
            email_to_display = data[website_to_search]["email"]
            password_to_display = data[website_to_search]["password"]

            messagebox.showinfo(title=website_to_search, message=f"Email: {email_to_display}\n"
                                                                 f"Password: {password_to_display}")
        else:
            messagebox.showinfo(title="Oops", message="No details for the website exists.")


# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=100, bg="white")

# Canvas
canvas = Canvas(width=200, height=250, highlightthickness=0, bg="white")
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", font=("Arial", 20, "normal"), highlightthickness=0, bg="white", fg="black")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", font=("Arial", 20, "normal"), highlightthickness=0, bg="white", fg="black")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=("Arial", 20, "normal"), highlightthickness=0, bg="white", fg="black")
password_label.grid(column=0, row=3)

# Entry boxes
website_box = Entry(width=20, highlightthickness=0, bg="white", fg="black")
website_box.grid(column=1, row=1)
website_box.focus()

email_box = Entry(width=35, highlightthickness=0, bg="white", fg="black")
email_box.grid(column=1, row=2, columnspan=2)
email_box.insert(0, "utsavkothari2002@gmail.com")

password_box = Entry(width=20, highlightthickness=0, bg="white", fg="black")
password_box.grid(column=1, row=3)

# Buttons
gen_pass_button = Button(text="Generate Password", width=11, highlightthickness=0, bg="white", command=gen_pass)
gen_pass_button.grid(column=2, row=3)

add_details_button = Button(text="Add", highlightthickness=0, bg="white", command=save)
add_details_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=11, highlightthickness=0, bg="white", command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()

#
# user_okay = messagebox.askokcancel(title="Title",
#                                            message=f"Are the details Ok?\n "
#                                                    f"Website: {website_entered}\n "
#                                                    f"Email: {email_entered}\n"
#                                                    f"Password: {password_entered}")


# Using Json
#
# with open('data.json', 'w') as data_file:
#     # Add data to a json file
#     json.dump(new_data, data_file, indent=4)
#
# with open('data.json', 'r') as data_file:
#     # Read data from json file
#     data = json.load(data_file)
#     print(data)
#
# with open('data.json', 'w') as data_file:
#     data.update(new_data)  # This data is what was retrieved from previous loading of data
#
#     json.dump(data, data_file, indent=4)  # Writing the data back where data contains the new_data
#
#     # data_file.write(f"{website_entered}  | {email_entered}  | {password_entered} \n")
#     website_box.delete(0, END)
#     email_box.delete(0, END)
#     password_box.delete(0, END)
