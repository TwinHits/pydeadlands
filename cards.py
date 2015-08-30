from random import randint, shuffle

class Deck:
    """A list of 54 cards.
            draw(): Returns 1 card, erases it from list. 
            shuffle(): Resets the deck to 54 cards in random order.
    """
    def __init__(self):
        self.cards = [Card(i) for i in range(1, 55)]
        self.shuffle()

    def draw(self):
        return self.cards.pop()

    def shuffle(self):
        self.cards = [Card(i) for i in range(1, 55)]
        self.shuffle()

class Card:
    """A card is really just a number. Takes a relative value of a card and
    looks it up on the card_lookup_table for the rest of the information.
            card.value: Get the relative value of the card.
            card.number: Get the number value of the card face
            card.suit: Get the relative value of the suit of the card face.
            card.die_num: Get the converted die num from the suit for character
            creation.
            card.die_size: Get the convereted die size from the number value for
            character creation.
            card.name: Get the name of the card face.
            """
    def __init__(self, value):
        self.value = value
        self.number = card_lookup_table[self.value][0]
        self.suit = card_lookup_table[self.value][1]
        self.die_num = card_lookup_table[self.value][2]
        self.die_size = card_lookup_table[self.value][3]
        if self.value == 1 or self.value == 54:
            self.name = self.number + " " + self.suit
        else:
            self.name = self.number + " of " + self.suit

card_lookup_table = {
        #number, suit, die number, die size for initilization of a deck
            1: ["Black", "Joker", 1, 12],
            2: ["Two", "Clubs", 1, 4],
            3: ["Two", "Diamonds", 2, 4],
            4: ["Two", "Hearts", 3, 4],
            5: ["Two", "Spades", 4, 4],
            6: ["Three", "Clubs", 1, 6],
            7: ["Three", "Diamonds", 2, 6],
            8: ["Three", "Hearts", 3, 6],
            9: ["Three", "Spades", 4, 6],
            10: ["Four", "Clubs", 1, 6],
            11: ["Four", "Diamonds", 2, 6],
            12: ["Four", "Hearts", 3, 6],
            13: ["Four", "Spades", 4, 6],
            14: ["Five", "Clubs", 1, 6],
            15: ["Five", "Diamonds", 2, 6],
            16: ["Five", "Hearts", 3, 6],
            17: ["Five", "Spades", 4, 6],
            18: ["Six", "Clubs", 1, 6],
            19: ["Six", "Diamonds", 2, 6],
            20: ["Six", "Hearts", 3, 6],
            21: ["Six", "Spades", 4, 6],
            22: ["Seven", "Clubs", 1, 6],
            23: ["Seven", "Diamonds", 2, 6],
            24: ["Seven", "Hearts", 3, 6],
            25: ["Seven", "Spades", 4, 6],
            26: ["Eight", "Clubs", 1, 6],
            27: ["Eight", "Diamonds", 2, 6],
            28: ["Eight", "Hearts", 3, 6],
            29: ["Eight", "Spades", 4, 6],
            30: ["Nine", "Clubs", 1, 8],
            31: ["Nine", "Diamonds", 2, 8],
            32: ["Nine", "Hearts", 3, 8],
            33: ["Nine", "Spades", 1, 8],
            34: ["Ten", "Clubs", 2, 8], 
            35: ["Ten", "Diamonds", 3, 8],
            36: ["Ten", "Hearts", 4, 8],
            37: ["Ten", "Spades", 1, 8],
            38: ["Jack", "Clubs", 2, 8],
            39: ["Jack", "Diamonds", 2, 8],
            40: ["Jack", "Hearts", 3, 8],
            41: ["Jack", "Spades", 4, 8],
            42: ["Queen", "Clubs", 1, 10],
            43: ["Queen", "Diamonds", 1, 10],
            44: ["Queen", "Hearts", 1, 10],
            45: ["Queen", "Spades", 1, 10],
            46: ["King", "Clubs", 1, 10],
            47: ["King", "Diamonds", 1, 10],
            48: ["King", "Hearts", 1, 10],
            49: ["King", "Spades", 1, 10],
            50: ["Ace", "Clubs", 1, 12],
            51: ["Ace", "Diamonds", 1, 12],
            52: ["Ace", "Hearts", 1, 12],
            53: ["Ace", "Spades", 1, 12],
            54: ["Red", "Joker", 1, 12]
        }

if __name__ == "__main__":
    d = Deck()
