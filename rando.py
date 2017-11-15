import random

#endo = 1
def get(endo):
#r = random.randint(1 , 10)

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
    print("Type a word and ye shall recieve a random number!")

    endo = input()

    num = len(endo)

    numb = (num * 2)

    total = random.randint(num , numb)

    return total

output = get("python")

print("thy number is" , output , "rejoice")
