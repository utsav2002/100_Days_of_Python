from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Entry box
input_box = Entry()
input_box.grid(column=1, row=0)

# Label
miles_label = Label(text="Miles", font=("Arial", 20, "normal"), width=7)
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to", font=("Arial", 20, "normal"))
is_equal_label.grid(column=0, row=1)

calc_answer = 0
answer_label = Label(text=calc_answer, font=("Arial", 20, "normal"))
answer_label.grid(column=1, row=1)

km_label = Label(text="Km", font=("Arial", 20, "normal"))
km_label.grid(column=2, row=1)


def cal_func():
    user_miles = input_box.get()
    calc_answer = round(float(user_miles) * 1.60934, 2)
    answer_label.config(text=calc_answer, font=("Arial", 20, "normal"))


# Button
calc_button = Button(text="Calculate", font=("Arial", 20, "normal"), command=cal_func)
calc_button.grid(column=1, row=2)

window.mainloop()
