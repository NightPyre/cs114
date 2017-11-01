import random
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

print("I'm definitely more of a fortune cookie than an 8ball, oh well .....please input your name")
name = input()
print("okay")
def getAnswer(answerNumber):

        if answerNumber == 1:
            return 'wow... I feel sorry for you after what I just saw'

        elif answerNumber == 2:
            return 'can you really afford to waste your short life using me?'

        elif answerNumber == 3:
            return 'bye, gotta go now'

        elif answerNumber == 4:
            return 'you will have fame and fortune and all that jazz'

        elif answerNumber == 5:
            return 'wanna play a game?'

        elif answerNumber == 6:
            return 'I forsee you continuing to seek my terrible fortunes'

        elif answerNumber == 7:
            return 'you will suffer a terrible accident(or not)'

        elif answerNumber == 8:
            return 'when trying to move forward, you will succeed only in moving back'

        elif answerNumber == 9:
            return 'you will find great fortune in hummus investments'

        elif answerNumber == 10:
            return 'vague and broad statement that feels like it applies to you'

        elif answerNumber == 11:
            return 'avoid italian food, it will be the death of you'

        elif answerNumber == 12:
            return 'good fortune follows you soon'

r = random.randint(1, 12)
fortune = getAnswer(r)
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(fortune)
