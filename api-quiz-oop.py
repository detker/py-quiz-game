import requests
import html

class Question:
    def __init__(self, category, questionStr, correctAnswerFlag):
        self.category = category
        self.questionStr = questionStr
        self.correctAnswerFlag = correctAnswerFlag

class Quiz:
    def __init__(self, questionsNum):
        self.apiUrl = "https://opentdb.com/api.php?category=9&difficulty=easy&type=boolean&amount="
        self.questionsNum = questionsNum
        self.questionsList = []
        self.loadQuestions(questionsNum)
    
    def loadQuestions(self, questionsNum):
        response = requests.get(self.apiUrl + str(questionsNum))
        if response.ok:
            data = response.json()["results"]
            for i in data:
                category = i["category"]
                questionStr = html.unescape(i["question"])
                correctAnswerFlag = i["correct_answer"].lower() in ["true", 1, "yes"]

                qObj = Question(category, questionStr, correctAnswerFlag)
                self.questionsList.append(qObj)
    
    def startQuiz(self):
        print("\nWelcome to Quiz!")
        numCorrectUserAnswer = 0
        n = 0
        numQuestions = len(self.questionsList)

        while n < numQuestions:
            q = self.questionsList[n]
            print("Question number:", n, ":", q.questionStr)
            # print("answerFlag:", q.correctAnswerFlag)

            answer = input("Give your answer: (y/n)")
            answerBool = False
            if answer == "y":
                answerBool = True
            if answerBool == q.correctAnswerFlag:
                print("Correct answer!")
                numCorrectUserAnswer += 1
            else:
                print("Incorrect answer!")
            
            n += 1
        
        print("Number of gained points:", numCorrectUserAnswer, "from", numQuestions, "questions.")

quiz = Quiz(10)
quiz.startQuiz()
