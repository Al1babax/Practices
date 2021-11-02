"""
Card deck class where Ace is treated as 14
Can create a deck and use shuffle function to shuffle the deck
"""

import random

SUITS = ("Hearts", "Diamonds", "Spades", "Clubs")
RANKS = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
VALUES = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 11,
    "Queen": 12,
    "King": 13,
    "Ace": 14
}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = VALUES[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in SUITS:
            for rank in RANKS:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):     # Returns one card value and removes from the top of the pile
        return self.all_cards.pop()


if __name__ == "__main__":
    pass
