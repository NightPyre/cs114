#Charmander_stats = {'hp': 20 , 'exp': 0 , 'level' : 5}
#charmander_moves = ['scratch' , 'growl']
#ohp = 20
import random

charmander = {
'HP' : 20 ,
'exp' : 0 ,
'level' : 5 ,
'scratch': 4,
'Def': 3
'name' : 'Charmander'
}

squirtle = {
'HP' : 20 ,
'exp' : 0 ,
'level' : 5 ,
'tackle': 4 ,
'Def': 3
'name' : 'Squirtle'
}

def attack(squirtle):
    rand_damage = random.randint(1,3)
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
            attack(oppo1)
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
