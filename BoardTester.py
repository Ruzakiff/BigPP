from Card import Card
from Board import Board

bb = Board()

card1 = Card("A", "s")
card2 = Card("Q", "s")

hand = [card1, card2]

bb.updateCards(hand)

print('hand')
for x in hand:
    print(x.rank + x.suit)
print()

print('hand on board')
for x in bb.cards:
    print(x.rank + x.suit)
print()

card3 = Card("3", "d")
card4 = Card("6", "s")
card5 = Card("T", "h")

flop = [card3, card4, card5]

print('flop')
for x in flop:
    print(x.rank + x.suit)
print()

flopAndHand = flop + hand

print('flop and hand')
for x in flopAndHand:
    print(x.rank + x.suit)
print()

bb.updateCards(flopAndHand)

print('flop and hand on board. hand should be ordered first')
for x in bb.cards:
    print(x.rank + x.suit)
print()


#dupCard1 = Card("A", "s")

dupCard1 = card1

flopAndHandWithDup = flopAndHand + [dupCard1]

print('flop and hand with duplicate')
for x in flopAndHandWithDup:
    print(x.rank + x.suit)
print()

bb.updateCards(flopAndHandWithDup)

print('flop and hand and dup on board. should have no dup')
for x in bb.cards:
    print(x.rank + x.suit)
print()

bb.clearCards()
print('cleared cards. should be empty')
for x in bb.cards:
    print(x.rank + x.suit)
print()


card8 = Card("J", "c")
card9 = Card("J", "h")
newHand = [card8, card9]
print('new hand')
for x in newHand:
    print(x.rank + x.suit)
print()

bb.updateCards(newHand)
print('new hand on board')
for x in newHand:
    print(x.rank + x.suit)
print()
