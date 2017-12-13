charmander = {
'HP' : 20 ,
'exp' : 0 ,
'level' : 5 ,
'scratch': 4,
'Def': 3,
'name' : 'Charmander' ,
#sets = ['1: scratch' , '2: growl']
}

squirtle = {
'HP' : 20 ,
'exp' : 0 ,
'level' : 5 ,
'tackle': 4 ,
'Def': 3,
'name' : 'Squirtle'
}

bulbasaur = {
'HP' : 20 ,
'exp' : 0 ,
'level' : 5 ,
'tackle': 4 ,
'Def': 3,
'name' : 'bulbasaur'
}

player1 = {
'Name' : 'red'
}

rival1 = {
'Rname' : 'blue'
}

#m = 0

import random
def intro():
    print("Hello there! Welcome to the world of Pokémon! My name is Oak! People call me the Pokémon Prof! This world is inhabited by creatures called Pokémon! For some people, Pokémon are pets. Other use them for fights. Myself… I study Pokémon as a profession. First, what is your name?")
    print(" ")
    print("Name?")
    player = input()
    player1['Name'] = player
    print(" ")
    print("Right! So your name is" , player , "! This is my grandson. He's been your rival since you were a baby. …Erm, what is his name again?")
    print(" ")
    print("Rival Name?")
    rival = input()
    rival1['Rname'] = rival
    print("That's right! I remember now! His name is" , rival , "!" , player , "! Your very own Pokémon legend is about to unfold! A world of dreams and adventures with Pokémon awaits! Let's go!")
    print(" ")
    print("Press Continue")
    cont = input()
    m = 0
    while m < 26:
        print(" ")
        m = m + 1

    print("*You wake up in your bed*")
    print("go downstairs? Y/N?")
    choose = input()

    if choose == 'N' or choose == 'No' or choose == 'no' or choose == 'n':
        #print("*You lay in bed for a while*")
        no()
    if choose == 'Y' or choose == 'Yes' or choose == 'yes' or choose == 'y':
        print("*you make your way to the livingroom*")
        print(" ")
        print("Go outside? Y/N?")

        choose = input()
        if choose == 'N' or choose == 'No' or choose == 'no' or choose == 'n':
            print("*you stand there*")

        if choose == 'Y' or choose == 'Yes' or choose == 'yes' or choose == 'y':
            print("*you make your way outside*")
            print("approach tall grass? (Y/N)")

            choose = input()

        if choose == 'N' or choose == 'No' or choose == 'no' or choose == 'n':
            print("*you stand there*")

        if choose == 'Y' or choose == 'Yes' or choose == 'yes' or choose == 'y':
            print("Hey! Wait! Don't go out! It's unsafe! Wild Pokémon live in tall grass! You need your own Pokémon for your protection. I know! Here, come with me!")
            print("*he grabs your arm and leads you to his lab, not far from your home*")
            print(" ")
            print("press Continue")
            cont = input()
            m = 0
            while m < 40:
                print(" ")
                m = m + 1
            print("*as you arrive in the lab you see a young man standing impatiently, he looks over at you and the man*")
            print(" ")
            print("Gramps! I'm fed up with waiting!")
            print(" ")
            print(rival, "? Let me think… Oh, that's right, I told you to come! Just wait! Here,", player , "! There are three Pokémon here. Haha! The Pokémon are held inside these Poké Balls. When I was young, I was a serious Pokémon Trainer. But now, in my old age, I have only these three left. You can have one. Go on, choose!")
            print(" ")
            print("Hey! Gramps! What about me?")
            print(" ")
            print("Be patient!" , rival , ". You can have one, too!")
            print(" ")
            print("Now," , player , ". Inside those three Poké Balls are Pokémon. Which one will you choose for yourself?")
            print(" ")
            print(" ")
            print("press continue")
            cont = input()
            m = 0
            while m < 15:
                print(" ")
                m = m + 1
            print("*you see three pokeballs on the table. charmander, squirtle, and bulbasaur*")
            print("which will you choose? (C/S/B)?")
            choose = input()
            starter = 0
            if choose == 'C' or choose == 'CHARMANDER' or choose == 'c' or choose == 'charmander' or choose == 'Charmander':
                print("You got CHARMANDER")
                starter = (starter + 1)
            if choose == 'S' or choose == 'SQUIRTLE' or choose == 'Squirtle' or choose == 's' or choose == 'squirtle':
                print("you got SQUIRTLE")
                starter = (starter + 2)
            if choose == 'B' or choose == 'BULBASAUR' or choose == 'b' or choose == 'bulbasaur' or choose == 'Bulbasaur':
                print("you got BULBASAUR")
                starter = (starter + 3)


            print("press continue")
            print(starter)
            cont = input()
            m = 0
            while m < 20:
                print(" ")
                m = m + 1
            print("*as you look at your new partner your rival grabs one of his own*")
            print("*he approaches and blocks your path* let's battle!")

            cont = input()
            m = 0
            while m < 20:
                print(" ")
                m = m + 1
            print("BATTLE START")
            #if starter == 1:

            #elif starter == 2:

            #elif starter == 3:

def game_over_first(char):
    print(charmander['name'] , "Has fainted, *The Professor steps in* that's enough you two. come here so I can heal your pokemon")


    #return sys.exit()
def game_over(char):
    print(charmander['name'] , "Has fainted, you white out")

#def part_2():





def move(charchar):
    sets = ['0: scratch' , '1: growl']
    print (sets)
    selection = int(input("Select 0 , 1"))
    if selection == 0:
        return charmander['scratch']

def attack(squirtle):
    i = input()
    if i == 'scratch':
        move
    pdamage = move(charmander)
    #rand_damage = random.randint(1,3)
    #squirtle['HP'] -= rand_damage
    squirtle['HP'] -= pdamage
    print(pdamage, " damage!")
    return squirtle

def attack2(squirtle):
    #i = input()
    #if i == 'scratch':
    #    move
    #pdamage = move(charmander)
    rand_damage = random.randint(2,6)
    squirtle['HP'] -= rand_damage

    print(rand_damage, " damage!")
    return squirtle

def fight(oppo1, oppo2):
    while (oppo1['HP'] > 0) and (oppo2['HP'] > 0):
        print(oppo1['name'], " attacks ", oppo2['name'])
        attack(oppo2)
        if oppo2['HP'] <= 0:
            print(oppo1['name'], " is winner")
            print('*your rival stares in shock* WHAT? Unbelievable! I picked the wrong Pokémon!')
            part_2()
        else:
            print(oppo2['name'], " attacks ", oppo1['name'])
            attack2(oppo1)
        if oppo1['HP'] <= 0:
            print(oppo2['name'], " is winner")
            print('*your rival laughs and smiles* Yeah! Am I great or what?')
            game_over_first(oppo1)
    print('charmander oppo1 HP: ', oppo1['HP'])
    print('squirtle oppo2 HP: ', oppo2['HP'])


def no():
    print("you chose to stay in bed for a while")

def encounter(charmander, squirtle):
    if charmander['HP'] >= 20:
        fight(charmander, squirtle)
        # if player['HP'] <= 0:
        #     return game_over(player)
def main():
        # fight(player, enemy1)

        # get_item(player)
    print('encounter 1...\n\n')
    encounter(charmander, squirtle)
intro()
main()

#def game_over(char):
    #print(charmander['name'] , "Has fainted, select a new pokemon")
    #return sys.exit()
