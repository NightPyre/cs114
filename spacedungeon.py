import random

print("===============Welcome to SPACE DUNGEON===================")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
input("////////////////////PRESS START////////////////////////////")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")

print("Before we begin, let's go over your files.")

print(" ")

Name = input("What is your name?")

print(" ")
print("So. you are" , Name , "?")
print(" ")
print(" ")

Class = input("What class are you?")

print("Interesting....you chose" , Class , "....very well. That matches the reccords")
print(" ")
print("How much health and Nano (nano is technology that grants you magic-like abilities) do you have?")
print("(It must add up to 100 between the two stats.)")
print(" ")
print("Health?")
Hp = int(input())
SHp = Hp

print(" ")
print("Nano?")

Mp = int(input())
SMp = Mp
bam = Hp + Mp
while bam > 100:
    print("uuh.. that doesn't sound right, maybe you should try again")
    print("Health?")
    Hp = int(input())
    SHp = Hp
    print(" ")
    print("Nano?")

    Mp = int(input())
    SMp = Mp
    bam = Hp + Mp

print(" ")
print("I see... let me be sure I have this right before we begin.")
print(" ")
print("So. You are" , Name , "the" , Class , "You have" , Hp , "Health, and" , Mp , "Nano.")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print("Press any button to continue..")




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




Any = input()

print("......")
print("......")
print("......")
print("......")
print("......")
print("......")
print("......")
print("......")
print("......")
print(" ")
print("*you begin your first fight*")
print("Health points:" ,Hp)
print("Nano:" ,Mp)
print(" ")
ohp = 100
print("enemy health" ,ohp)

while Mp > 0 and ohp > 0 and Hp > 0:

    r = random.randint(1, 4)
    r2 = random.randint(10, 25)
    print("do you cast a spell? (Y/N)")
    an = input()
    if an == "y":
        Mp = Mp - 10
        print("you use a nano-tech")
        print(" ")
        print("you have" , Mp , "Nano remaining")
        for whatever in range(1):
            print("")
            print(" ")

             #subtract 10 from health
            ohp = ohp - r2

            Hp = Hp - r
             #print out health
            print("you have" ,Hp, "health left")
            print("enemy has" ,ohp, "health left")




        pass

    if an == "n":
        mp = mp
        print("you do not cast a spell")
        print(" ")
        print("you have" , mp , "mana remaining")

#print("You have run out of oxygen")
#print(" ")
if Hp < 0 and Mp < 0:

    print("......................YOU HAVE DIED........................")
    print("Press any button to continue..")
    Any = input()
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print("///////////THANK YOU for playing the Space Dungeon demo////////////")

elif ohp < 0:
    print("You win! ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print("restoring health and nano")
    Hp = SHp
    Mp = SMp
    print("you have" , Hp , "health, and" , Mp , "nano")
    Any = input()
    print("Press any button to continue..")
    Any = input()
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print("///////////THANK YOU for playing the Space Dungeon demo////////////")
