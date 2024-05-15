from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for questions in question_data:
    new_q = Question(question_text=questions['text'], question_answer=questions['answer'])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}.")
