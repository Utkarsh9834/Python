# Exercise 4
# Pattern Printing
# Input = Integer n
# Boolean = True or False
#
# True n=5
# *
# **
# ***
# ****
#
# False n=5
# ****
# ***
# **
# *
n = int(input("Enter numbers of row :"))
print("Press 1 or 0 ")
bool_num = input("1 for true and 0 for false")
if bool_num == "1":
    for i in range(0, n+1):
        print("*"*i)
if bool_num == "0":
    for i in range(n, 0, -1):
        print("*"*i)