mp = 50
hp = 50

print("health points:" ,hp)
print("mana:" ,mp)
print(" ")
print(" ")
while mp > 0:


    print("do you cast a spell? (Y/N)")
    an = input()
    if an == "y":
        mp = mp - 10
        print("you cast a spell")
        print(" ")
        print("you have" , mp , "mana remaining")
        for whatever in range(1):
            print("your spell backfires")
            print(" ")

             #subtract 10 from health
            hp = hp - 10
             #print out health
            print("you have" ,hp, "health left")




        pass

    if an == "n":
        mp = mp
        print("you do not cast a spell")
        print(" ")
        print("you have" , mp , "mana remaining")

    #for whatever in range(1):
        #print("your spell backfires")
        #print(" ")

         #subtract 10 from health
        #hp = hp - 10
         #print out health
        #print("you have" ,hp, "health left")
