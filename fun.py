from random import randint

countCommon = 0
countRare = 0
countEpic = 0
countLegendary = 0

def probOut():
    print("\t3 Items In One Pack")
    print("\tCommon       50% Probability")
    print("\tRare         30% Probability")
    print("\tEpic         13% Probability")
    print("\tLegendary    7% Probability")


def packOpen():
    global countCommon
    global countRare
    global countEpic
    global countLegendary

    for num in range(0,3):
        lcNum =randint(0,100)
        if (lcNum <= 7):
            print("\tYou Got A Legendary Item\n")
            countLegendary +=1
        elif(lcNum <=20):
            print("\tYou Got An EPic Item\n")
            countEpic +=1
        elif (lcNum <=50):
            print("\tYou Got A Rare Item\n")
            countRare +=1
        else:
            print("\tYou Got A Common Item\n")
            countCommon +=1
    
def itemSum():
    print("You Got Total of\t :\n")
    print("\tLegendary     :",countLegendary)
    print("\tEpic          :",countEpic)
    print("\tRare          :",countRare)
    print("\tCommon        :",countCommon)