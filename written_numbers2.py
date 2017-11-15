def main():
    print("please input a number between 1 and 99")
    num = int(input())
    tens = num // 10
    ones = num % 10

    def getTens(answerNumber):
        if tens == 1:
            return 'ten'

        elif tens == 2:
            return 'twenty'

        elif tens  == 3:
            return 'thirty'

        elif tens  == 4:
            return 'forty'

        elif tens == 5:
            return 'fifty'

        elif tens  == 6:
            return 'sixty'

        elif tens  == 7:
            return 'seventy'

        elif tens  == 8:
            return 'eighty'

        elif tens  == 9:
            return 'ninty'
    ten = getTens(tens)

    def getOnes(answerNumbers):
        if ones == 1:
            return 'one'

        elif ones == 2:
            return 'two'

        elif ones == 3:
            return 'three'

        elif ones  == 4:
            return 'four'

        elif ones == 5:
            return 'five'

        elif ones  == 6:
            return 'six'

        elif ones == 7:
            return 'seven'

        elif ones  == 8:
            return 'eight'

        elif ones  == 9:
            return 'nine'
    one = getOnes(ones)
    def getodds(answerNumberss):
        if tens == 0:
            output = ones
        elif tens == 1:
            if ones == 1:
                output = 'eleven'
            elif ones == 2:
                output = 'twelve'
            elif ones == 3:
                output = 'thirteen'
            elif ones == 5:
                output = 'fifteen'
            elif ones == 0:
                output = 'ten'
            else:
                output = one + 'teen'
        else:
            output = tens+ '-' + ones

            print(output)

getOnes()
getTens()
getodds()
if num < 10:
    print(one)

else:
     print (ten + one)

main()
