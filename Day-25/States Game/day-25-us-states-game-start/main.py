import turtle
from turtle import Screen

import pandas as pd

screen = Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

correct_state_list = []

df = pd.read_csv("50_states.csv")
states_list = df.state.to_list()
x_co_ordinate_list = df.x.to_list()
y_co_ordinate_list = df.y.to_list()

states_to_learn = states_list

game_is_on = True

while game_is_on and (len(states_list)) < 51:

    user_answer = str(screen.textinput(title=f" {len(correct_state_list)}/50 States Correct", prompt="What's another state's name?: ").title())

    if user_answer == "Exit":

        states_to_learn.insert(0, "States You Should Learn: ")

        states_list_df = pd.DataFrame(states_to_learn)
        states_list_df.to_csv('states_to_learn.csv')

        break

    # Check if state exists:
    elif user_answer in states_list:
        index_of_state = (states_list.index(user_answer))    # Index of the state
        x_co_ordinate = x_co_ordinate_list[index_of_state]
        y_co_ordinate = y_co_ordinate_list[index_of_state]

        # write name of the state
        state_name_writer = turtle.Turtle()
        state_name_writer.hideturtle()
        state_name_writer.penup()
        state_name_writer.goto(x_co_ordinate, y_co_ordinate)
        state_name_writer.write(f"{user_answer}", font=("Verdana", 10, "normal"))

        # add name of the state to correct state list:
        correct_state_list.append(user_answer)

        # remove user answer from states to learn:
        states_to_learn.remove(user_answer)

screen.mainloop()

# Making the CSV file for states_to_learn using comprehension List
# missing_states = [(missing_state.append(state)) for state in all_state if (state not in guessed_states)]
