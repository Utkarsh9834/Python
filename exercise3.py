#Number Guessing Game
#unlimited chanche we get
"""
print("Welcome To Number Guessing Game")
print()
num = 5
while (True):
    print("Enter your guess number")
    user = int(input())
    if num < user :
        print("Your number should be less Please enter small number")
        continue
    elif num > user :
        print("your number should be big, Please enter large number")
        continue
    elif num == user :
        print("You guess correct number")
        print("YOU WIN !!!")
        break
"""
# for limited chanche
print("Welcome To Number Guessing Game")
print()
num = 5
limit = 1
print("Number of guesses is limited to only 9 times:")
while (limit <= 5):
    limit = limit + 1
    print("Enter your guess number")
    user = int(input())
    if num < user :
        print("Your number should be less Please enter small number")

    elif num > user :
        print("your number should be big, Please enter large number")

    else:
        print("You guess correct number")
        print("YOU WON !!!")
        #print(chanche," no. of guesses left")


        print(6 - limit, "no. of guesses left")
        break

if (limit > 5):
    print("Game Over")

