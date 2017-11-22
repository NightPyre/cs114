import random

def getenemy():

    r = random.randint(0, 3)
    spam = ["kobold","space pirate"," rogue commando","robo-soldier"]
    fight = spam[r]
    print ("Your attacker is", fight)

print("You are ambushed in space!!!")

choice = input()
print(" ")
print(" ")
getenemy()
#print("Your attacker is", spam[r])
#def main():
#main()
