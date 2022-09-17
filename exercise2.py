# Exercise 2 - Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result
print(" 1 for multiplication , 2 for addition , 3 for divison")
mode = int(input())
print("Enter ur two number for operation")
a = int(input())
print("next number")
b = int(input())
print()
if a==45 and b==3 and mode==1:
    print(555)
elif a==56 and b==9 and mode==2:
    print(77)
elif a==56 and b==6 and mode==3:
    print(4)
elif mode==1:
    calculation=a*b
    print(calculation)
elif mode == 2:
    calculation = a + b
    print(calculation)
elif mode == 3:
    calculation = a / b
    print(calculation)
else:
    print("default!!!")