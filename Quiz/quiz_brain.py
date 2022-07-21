class QuizBrain:
    #questions access questionBank List
    def __init__(self,questions):
        self.questionNumber=0
        self.questions=questions
        self.score=0

    def stillQuestions(self):
        return self.questionNumber<len(self.questions)

    def nextQuestion(self):
        #List have both Text and answer accessed through indexing
        currentQuestion=self.questions[self.questionNumber]
        self.questionNumber+=1
        user=input(f"Q. {self.questionNumber}{currentQuestion.text}(True/False): ")
        self.checkAnswer(user,currentQuestion.answer)

    def checkAnswer(self,userAnswer,correctAnswer):
        if userAnswer.lower()==correctAnswer.lower():
            self.score+=1
            print("You're Correct!")
        else:
            print("You're wrong!")
        print(f"Current Score {self.score}/{self.questionNumber}")
        print(f"Correct answer is {correctAnswer}")
        print("\n")



