from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

q_bank = []
for question in question_data:
    text_bank = question["text"]
    answer_bank = question["answer"]
    new_question = Question(text_bank, answer_bank)
    q_bank.append(new_question)

quiz = Quizbrain(q_bank)

while quiz.still_has_question():
    quiz.nextquestion()

print("you have completed the task")
print(f"your total score was {quiz.score} / {quiz.question_number}")
