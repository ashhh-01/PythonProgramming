from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questionBank=[]
for questions in question_data:
    question=questions["text"]
    answer=questions["answer"]
    newQuestion=Question(question,answer)
    questionBank.append(newQuestion)

quiz=QuizBrain(questionBank)
while quiz.stillQuestions():
    quiz.nextQuestion()
print("Congragulations!You completed the quiz")
print(f"Final Score: {quiz.score}/{quiz.questionNumber}")