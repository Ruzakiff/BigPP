class Card:
    def _init_(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def getSuit(self):
        return self.suit

    def getRank(self):
        return self.rank