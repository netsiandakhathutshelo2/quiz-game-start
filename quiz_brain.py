class Quizbrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def nextquestion(self):
        current = self.question_list[self.question_number]
        self.question_number += 1
        user = input(f"Q.{self.question_number}:{current.text} (true/false)?")
        self.check_answer(user, current.answer)

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("your answer is correct")
        else:
            print(f"That's wrong, the correct answer is {correct_answer} ")
        print(f"your total score is {self.score} / {len(self.question_list)}")
        print("/n")
