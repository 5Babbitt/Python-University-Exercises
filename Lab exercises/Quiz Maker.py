quiz = []

def CreateQuiz():
    numQ = int(input("Enter number of Questions (minimum 5): "))

    for i in range(numQ):
        
        tempQuestion = []
        
        Q = input("Enter Question: ")
        A = input("Enter Option A: ")
        B = input("Enter Option B: ")
        C = input("Enter Option C: ")
        D = input("Enter Option D: ")
        answer = input("Enter Correct Answer option: ")

        tempQuestion.append('Question: ' + Q)
        tempQuestion.append('A. ' + A)
        tempQuestion.append('B. ' + B)
        tempQuestion.append('C. ' + C)
        tempQuestion.append('D. ' + D)
        tempQuestion.append('Answer: ' + answer)

        quiz.append(tempQuestion)
        print(quiz)

def SaveQuiz():
    file = open('quiz.txt', 'w')
    for question in quiz:
        for i in range(6):
            file.write(question[i] + '\n')
        file.write('\n')

def TakeQuiz():
    
    file = open('quiz.txt', 'r')
    content = file.read()
    print(content)
    for i in range(5):
        print(quiz[i])

TakeQuiz()

        