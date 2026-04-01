questions = [
    "What is the capital of India?",
    "Which language is used to write Python programs?",
    "What is 2 + 2?"
    ]

answers = [
    "Delhi",
    "Python",
    "4"
]

money = [1000, 2000, 3000]

amount = 0 

print("Welcome to the KBC game\n")

for i in range(len(questions)):
    print(questions[i])
    user_ans = input("Your answer: ")

    if user_ans == answers[i]:
         amount = money[i]
         print("Correct answers!\n")
      
    else:
         print("Wrong answer")
         break
    
print("You won the prize of amount:",amount)
