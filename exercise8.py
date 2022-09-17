import os
print("Oh Soldier Prettify My Folder\n")
def solid(a,b,c):
    os.chdir(a)
    d = os.listdir(a)
    for item in d:
        x = os.rename(item,item.capitalize())


a = input("Enter your path")
print(os.listdir(a))
b = input("Enter ur directory file")
c = input("Enter format type")
solid(a,b,c)
