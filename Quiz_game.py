
#The first array to hold the questions

Questions = [
    "1. What is the name of the mother of Jesus?",
    "2. Who killed Goliath?",
    "3. Who saw a burning bush?"
]
options = [
    ["A. Martha B. Mary C. Naomi D. Ruth"],
    ["A. David B. James C. Samson D. Peter"],
    ["A. Moses B. Jethro C. Mathew D. James"]
]
answers = ['B' ,'A' ,'A']

def quiz(x ,y ,z):
    count = 0
    for i in range(len(x)):
        print(x[i])
        for u in y[i]:
            print(u)
        users = input("Enter your answer: ").upper()
        if users == answers[i]:
            print("Correct")
            count = count + 1
        else:
            print("Incorrect")
    score = (count / len(x)) * 100
    print("Your score is", score, "%")

quiz(Questions,options, answers)
