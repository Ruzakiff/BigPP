from eyes import foundCards
#import eyes
from Card import Card

#S, C, H, D
cardObjects=[[
Card('A', 's'), Card('2', 's'),
Card('3', 's'), Card('4', 's'),
Card('5', 's'), Card('6', 's'),
Card('7', 's'), Card('8', 's'),
Card('9', 's'), Card('10', 's'),
Card('J', 's'), Card('Q', 's'),
Card('K', 's'),
],
[
Card('A', 'c'), Card('2', 'c'),
Card('3', 'c'), Card('4', 'c'),
Card('5', 'c'), Card('6', 'c'),
Card('7', 'c'), Card('8', 'c'),
Card('9', 'c'), Card('10', 'c'),
Card('J', 'c'), Card('Q', 'c'),
Card('K', 'c'),
],
[
Card('A', 'h'), Card('2', 'h'),
Card('3', 'h'), Card('4', 'h'),
Card('5', 'h'), Card('6', 'h'),
Card('7', 'h'), Card('8', 'h'),
Card('9', 'h'), Card('10', 'h'),
Card('J', 'h'), Card('Q', 'h'),
Card('K', 'h'),
],
[
Card('A', 'd'), Card('2', 'd'),
Card('3', 'd'), Card('4', 'd'),
Card('5', 'd'), Card('6', 'd'),
Card('7', 'd'), Card('8', 'd'),
Card('9', 'd'), Card('10', 'd'),
Card('J', 'd'), Card('Q', 'd'),
Card('K', 'd'),
]]

#print("")
#returns list of cards
def getListOfCardObjectsFromImages():
    cardListToReturn=[]
    for i in range(len(foundCards)):
        for j in range(len(foundCards[i])):
            if foundCards[i][j] == true:
                cardListToReturn.append(cardObjects[i][j])
                print("Cards:"+cardObjects[i][j])
    return cardListToReturn
