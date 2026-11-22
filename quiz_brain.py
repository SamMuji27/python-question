class QuizBrain:
    def __init__(self, list_question):
        self.q_list = list_question
        self.q_number = 0
        self.score = 0

    def next_question(self):
        data_question = self.q_list[self.q_number]
        self.q_number += 1
        user_answer = input(f"Q.{self.q_number}: {data_question.q_text} (True/False):")
        real_answer = data_question.q_answer
        self.check_answer(user_answer, real_answer)

    def any_question(self):
        if self.q_number < len(self.q_list):
            return True

    def check_answer(self, user_answer, real_answer):
        if user_answer.lower() == real_answer.lower():
            self.score += 1
            print("you got it!")
            print(f"score: {self.score} \n")

        else:
            print("your answer is wrong!")
            print(f"last score: {self.score}/{self.q_number} \n")
