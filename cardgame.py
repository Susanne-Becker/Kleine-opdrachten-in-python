# Implements a cards shuffler and dealer.
import random

ALPHA = 26

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def description(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self._suits = ['Hearts','Diamonds','Clubs','Spades']
        self._values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self._cards = []
        for suit in self._suits:
            for value in self._values:
                 self._cards.append(Card(suit, value))
       

    def description(self):
        return f"{len(self._cards)} cards in the deck"


    def shuffle(self):
        for i in range(len(self._cards)-1, 0, -1):
            r = random.randint(0, i)
            self._cards[i], self._cards[r] = self._cards[r], self._cards[i]

    def deal(self):
        return self._cards.pop()

if __name__ == "__main__":
    deck = Deck()
    card = deck.deal()
    print(card.description())