# Health Management System
# 3 clients - Garry, Rohan and Hammad
# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client
def getdate():
    import datetime
    return datetime.datetime.now()


print("Health Management System")
print("1 for Garry, 2 for Rohan, 3 for Hammad\n")
n = int(input())
print("1 for Log and 2 for Retrive \n")
k = int(input())
if k == 1:
    if n == 1:
        c = int(input("enter 1 for excersise and 2 for food"))
        if c == 1:
            with open("Garry_exercise.txt", "a") as op:
                op.write(str([getdate()]))
                op.write(input("what did you exercise : "))
                op.close()
            print("You Entered successfully in Garry Exercise file")
        elif c == 2:
            with open("Garry_Food.txt", "a") as op:
                op.write(str([getdate()]))
                op.write(input("What did you Eat : "))
                op.close()
            print("You Entered successfully in Garry Food file")
    elif n == 2:
        c = int(input("enter 1 for excersise and 2 for food"))
        if c == 1:
            with open("Rohan_exercise.txt", "a") as op:
                op.write(str([getdate()]))
                op.write(input("what did you exercise : "))
                op.close()
            print("You Entered successfully in Garry Exercise file")
        elif c == 2:
            with open("Rohan_Food.txt", "a") as op:
                op.write(str([getdate()]))
                op.write(input("What did you Eat : "))
                op.close()
            print("You Entered successfully in Garry Food file")
    elif n == 3:
        c = int(input("enter 1 for excersise and 2 for food"))
        if c == 1:
            with open("Hammad_exercise.txt", "a") as op:
                op.write(str([getdate()]))
                op.write(input("what did you exercise : "))
                op.close()
            print("You Entered successfully in Garry Exercise file")
        elif c == 2:
            with open("Hammad_Food.txt", "a") as op:
                op.write(str([getdate()]))
                op.write(input("What did you Eat : "))
                op.close()
            print("You Entered successfully in Garry Food file")
    else:
        print("plz enter valid input (Garry,Rohan,Hammad)")
elif k == 2:
    if n == 1:
        q = int(input("enter 1 for excersise and 2 for food"))
        if q == 1:
            with open("Garry_exercise.txt") as op:
                for i in op:
                    print(i, end="")
                op.close()
        elif q == 2:
            with open("Garry_Food.txt") as op:
                for i in op:
                    print(i, end="")
                op.close()
    elif n == 2:
        q = int(input("enter 1 for excersise and 2 for food"))
        if q == 1:
            with open("Rohan_exercise.txt") as op:
                for i in op:
                    print(i, end="")
                op.close()
        elif q == 2:
            with open("Rohan_Food.txt") as op:
                for i in op:
                    print(i, end="")
                op.close()
    elif n == 3:
        q = int(input("enter 1 for excersise and 2 for food"))
        if q == 1:
            with open("Hammad_exercise.txt") as op:
                for i in op:
                    print(i, end="")
                op.close()
        elif q == 2:
            with open("Hammad_Food.txt") as op:
                for i in op:
                    print(i, end="")
                op.close()
    else:
        print("plz enter valid input (Garry,Rohan,Hammad)")
else:
    print("Invalid Input")