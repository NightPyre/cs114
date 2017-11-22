import random
#answerNumber = 10
def getAnswer():

    r = random.randint(0, 8)
    fortunea = ['can you really afford to waste your short life using me?',
    'you will have fame and fortune and all that jazz',
    'I forsee you continuing to seek my terrible fortunes',
    'you will suffer a terrible accident(or not)',
    'when trying to move forward, you will succeed only in moving back',
    'you will find great fortune in hummus investments',
    'vague and broad statement that feels like it applies to you',
    'avoid italian food, it will be the death of you',
    'good fortune follows you soon'
    ]
    print(fortunea[r])
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print("I'm definitely more of a fortune cookie than an 8ball, oh well .....please input your name")
    name = input()
    print("okay")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print("well",name,".",fortunea[r])
getAnswer()
