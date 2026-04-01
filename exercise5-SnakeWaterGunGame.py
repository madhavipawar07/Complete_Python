import random 

def check(user,comp):

    if comp == user:
        return 0
    
    if user == 1 and comp == 0:
        return -1
    
    if user == 0 and comp == 2:
        return -1
    
    if user == 2 and comp == 1:
        return -1
    
    return 1


comp = random.randint(0,2)

user = int(input("0 for Snake, 1 for Water and 2 for Gun: "))

print("Your choice: ",user)
print("Computer's choice: ",comp)

score = check(user, comp)

if score ==0:
    print("It's a draw..")


elif(score == -1):
    print("You lose..")

else:
    print("You win !")