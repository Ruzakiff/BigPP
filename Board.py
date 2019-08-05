class Board:

    def __init__(self):
        self.potSize = 0
        self.cards = []

    def updateCards(self, cardList):
        for c in cardList:
            if c not in self.cards:
                self.cards.append(c)

    def clearCards(self):
        self.cards.clear()
