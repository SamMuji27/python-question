from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

all_question = []
for question in question_data:
    q_text = question["text"]
    q_answer = question["answer"]
    question_data = Question(q_text, q_answer)
    all_question.append(question_data)

quiz_brain = QuizBrain(all_question)

while quiz_brain.any_question():
    quiz_brain.next_question()


