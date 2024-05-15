from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.answer = None
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        # Labels

        self.score_label = Label(text=f"Score: 0", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        # Canvas
        self.canvas = Canvas(width=400, height=400, bg="white")
        self.question_text = self.canvas.create_text(
            200, 205, text="Random question", font=('Arial', 25, 'italic'), fill=THEME_COLOR,
            width=200, justify=CENTER)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Button
        right_img = PhotoImage(file='images/true.png')
        wrong_img = PhotoImage(file='images/false.png')

        self.right_button = Button(image=right_img, highlightthickness=0, command=self.check_true)
        self.right_button.grid(column=0, row=2)

        self.wrong_button = Button(image=wrong_img, highlightthickness=0, command=self.check_false)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()

        self.check_true()
        self.check_false()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"All questions completed, your final score is "
                                                            f"{self.quiz.score}/{self.quiz.question_number}")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def check_true(self):
        self.answer = "true"
        correct_or_not = self.quiz.check_answer(self.answer)

        self.give_feedback(correct_or_not)

    def check_false(self):
        self.answer = "false"
        correct_or_not = self.quiz.check_answer(self.answer)

        self.give_feedback(correct_or_not)

    def give_feedback(self, correct_or_not):
        if correct_or_not:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
