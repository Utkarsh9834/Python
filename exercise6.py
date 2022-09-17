# Snake water gun
# Create a snake water gun game in Python! Search Snake water gun game in google if you need help on rules and how to play the game!
print("                                Welcome to Snake Water Gun                                             ")
print("Rules:-")
print("\t\tSnake vs. Water: Snake drinks the water hence wins.\n\t\tWater vs. Gun: The gun will drown in water, hence a point for water.\n\t\tGun vs. Snake: Gun will kill the snake and win.\n")
chance = 10
no_of_chance = 0
computer_point = 0
human_point = 0
import random
game = ["S", "W", "G"]
#print(comp)
print("Enter your choice from given below:-\n\n\t\t 'S' for Snake\n\t\t 'W' for Water\n\t\t 'G' for Gun\n" )
print("Your input must be in Capital character\n")
while no_of_chance<=chance:
    human = input("Snake Water Gun\n")
    comp = random.choice(game)
    if human == comp:
        print(f"your guess {human} and computer guess is {comp} \n")
        print("!!! Game Tie !!!\n Both get 0 point\n")
        # user input if S
    elif human == "S" and comp == "G":
        computer_point=computer_point+1
        print(f"your guess {human} and computer guess is {comp} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")
    elif human == "S" and comp == "W":
        human_point = human_point + 1
        print(f"your guess {human} and computer guess is {comp} \n")
        print("You wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")
        # user input if W
    elif human == "W" and comp == "S":
        computer_point=computer_point+1
        print(f"your guess {human} and computer guess is {comp} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")
    elif human == "W" and comp == "G":
        human_point = human_point + 1
        print(f"your guess {human} and computer guess is {comp} \n")
        print("You wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")
        #user input if G
    elif human == "G" and comp == "W":
        computer_point=computer_point+1
        print(f"your guess {human} and computer guess is {comp} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")
    elif human == "G" and comp == "S":
        human_point = human_point + 1
        print(f"your guess {human} and computer guess is {comp} \n")
        print("You wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")
    else:
        print("Invalid Input")
    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance} \n")
print("Game over")

if computer_point==human_point:
    print("Tie")

elif computer_point > human_point:
    print("Victory Goes to Computer")
else:
    print("Victory Goes to You")
print(f"your point is {human_point} and computer point is {computer_point}")
