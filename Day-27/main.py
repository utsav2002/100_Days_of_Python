from tkinter import *

def button_clicked():
    input_data = input_box.get()
    my_label.config(text=input_data)


window = Tk()
window.title("GUI PROGRAM")
window.minsize(width=500, height=300)
window.config(padx=20,pady=20)

# Label
my_label = Label(text="I am a Label", font=("Arial", 20, "bold"))
my_label.grid(column=0, row=0)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# New Button
button2 = Button(text="I am a new Button")
button2.grid(column=2, row=0)

# Entry
input_box = Entry()
print(input_box.get())
input_box.grid(column=3, row=2)

window.mainloop()
