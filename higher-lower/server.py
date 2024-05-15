import time

from flask import Flask
import random

app = Flask(__name__)

random_page = random.randint(0, 9)

@app.route('/')
def main_page():
    return f"<h1><b>Guess a number between 0 and 9</b></h1>" \
           f"<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


@app.route(f'/<int:random_num>')
def show_page(random_num):
    if random_num > random_page:
        return f"<h1><b>Too high! Try Again!</b></h1>" \
               f"<img src=https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif>"
    elif random_num < random_page:
        return f"<h1><b>Too Low! Try Again!</b></h1>" \
               f"<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    else:
        return f"<h1><b>You Found Me!</b></h1>" \
               f"<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


keep_playing = True

while keep_playing:
    if __name__ == "__main__":
        app.run(debug=True)