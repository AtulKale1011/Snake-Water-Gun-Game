"""
GAME:
SNAKE WATER GUN
SNAKE:1
WATER :-1
GUN :0
userDict = {"s": 1,"w":-1, "g" : 0}
userDict = {"snake" or "s" or "Snake" or "SNAKE": 1,"WATER" or "water" or "Water" or"w":-1, "g" or "gun" or "Gun" or "GUN": 0}
"""
import random


computer = random.choice([1, 0, -1])

userStr = input("Enter Your Choice :")

userDict = {"snake": 1,"water":-1, "gun" : 0, "SNAKE" : 1, "WATER": -1, "GUN": 0, "s": 1,"w":-1, "g" : 0, "Snake": 1,"Water":-1, "Gun" : 0, "S": 1,"W":-1, "G" : 0}


reverseDict = { 1:"snake", -1:"water", 0:"gun"}


you = userDict[userStr]

print(f" \n  You Chose: {reverseDict[you]} \n \n  Computer Chose: {reverseDict[computer]} \n")

if(computer == -1 and you == 1):
    print("BRAVO YOU WON! \n")


elif(computer == -1 and you == 0):
    print("BOO YOU LOST! \n")

elif(computer == -1 and you == -1):
    print("IT'S A TIE \n")  


elif(computer == 1 and you == 0):
    print("BRAVO YOU WON! \n")


elif(computer == 1 and you == -1):
    print("BOO YOU LOST! \n")

elif(computer == 1 and you == 1):
    print("IT'S A TIE \n")



elif(computer == 0 and you == -1):
    print("BRAVO YOU WON! \n")


elif(computer == 0 and you == 1):
    print("BOO YOU LOST! \n")

elif(computer == 0 and you == 0):
    print("IT'S A TIE \n") 

else:
    print("somethig went wrong")






