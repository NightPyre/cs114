import random

def getAnswer(answerNumber):

    r = random.randint(1, 9)
    if answerNumber == 1:
        return 'can you really afford to waste your short life using me?'

    elif answerNumber == 2:
        return 'you will have fame and fortune and all that jazz'


    elif answerNumber == 3:
        return 'I forsee you continuing to seek my terrible fortunes'

    elif answerNumber == 4:
        return 'you will suffer a terrible accident(or not)'

    elif answerNumber == 5:
        return 'when trying to move forward, you will succeed only in moving back'

    elif answerNumber == 6:
        return 'you will find great fortune in hummus investments'

    elif answerNumber == 7:
        return 'vague and broad statement that feels like it applies to you'

    elif answerNumber == 8:
        return 'avoid italian food, it will be the death of you'

    elif answerNumber == 9:
        return 'good fortune follows you soon'
def main():
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
    r2 = random.randint(1, 9)
    result = getAnswer(r2)
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print("well" , name , "." , result)
main()
