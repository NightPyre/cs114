#Charmander_stats = {'hp': 20 , 'exp': 0 , 'level' : 5}
#charmander_moves = ['scratch' , 'growl']
#ohp = 20
import random

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

def game_over(char):
    print(charmander['name'] , "Has fainted, select a new pokemon")
    return sys.exit()


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
        else:
            print(oppo2['name'], " attacks ", oppo1['name'])
            attack2(oppo1)
        if oppo1['HP'] <= 0:
            print(oppo2['name'], " is winner")
            game_over(oppo1)
    print('charmander oppo1 HP: ', oppo1['HP'])
    print('squirtle oppo2 HP: ', oppo2['HP'])

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
main()
#def game_over(char):
    #print(charmander['name'] , "Has fainted, select a new pokemon")
    #return sys.exit()
