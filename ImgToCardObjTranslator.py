from eyes import foundCards
from Card import Card

#s, c, h, d
cardObjects=[[
new Card('A', 's'), new Card('2', 's'),
new Card('3', 's'), new Card('4', 's'),
new Card('5', 's'), new Card('6', 's'),
new Card('7', 's'), new Card('8', 's'),
new Card('9', 's'), new Card('10', 's'),
new Card('J', 's'), new Card('Q', 's'),
new Card('K', 's'),
],
[
new Card('A', 'c'), new Card('2', 'c'),
new Card('3', 'c'), new Card('4', 'c'),
new Card('5', 'c'), new Card('6', 'c'),
new Card('7', 'c'), new Card('8', 'c'),
new Card('9', 'c'), new Card('10', 'c'),
new Card('J', 'c'), new Card('Q', 'c'),
new Card('K', 'c'),
],
[
new Card('A', 'h'), new Card('2', 'h'),
new Card('3', 'h'), new Card('4', 'h'),
new Card('5', 'h'), new Card('6', 'h'),
new Card('7', 'h'), new Card('8', 'h'),
new Card('9', 'h'), new Card('10', 'h'),
new Card('J', 'h'), new Card('Q', 'h'),
new Card('K', 'h'),
],
[
new Card('A', 'd'), new Card('2', 'd'),
new Card('3', 'd'), new Card('4', 'd'),
new Card('5', 'd'), new Card('6', 'd'),
new Card('7', 'd'), new Card('8', 'd'),
new Card('9', 'd'), new Card('10', 'd'),
new Card('J', 'd'), new Card('Q', 'd'),
new Card('K', 'd'),
]]

#returns list of cards
def getListOfCardObjectsFromImages(){
    cardListToReturn=[]
    for i in range(len(foundCards)):
        for j in range(len(foundCards[i])):
            if foundCards[i][j] == true:
                cardListToReturn.append(cardObjects[i][j])
    return cardListToReturn
    
}