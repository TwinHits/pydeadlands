from random import randint, shuffle

class Deck:
    """A list of 54 cards.
            draw(): Returns 1 card, erases it from list. 
            shuffle(): Resets the deck to 54 cards in random order.
    """
    def __init__(self):
        self.shuffle()

    def draw(self):
        return self.cards.pop()

    def shuffle(self):
        self.cards = [Card(i) for i in range(1, 55)]
        shuffle(self.cards)

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
        lookup = card_lookup_table[self.value] 
        self.number = lookup[0]
        self.suit = lookup[1]
        self.die_num = lookup[2]
        self.die_size = lookup[3]
        if self.value == 53 or self.value == 54:
            self.name = self.number + " " + self.suit
        else:
            self.name = self.number + " of " + self.suit

card_lookup_table = {
        #number, suit, die number, die size for initilization of a deck
            1: ["Two", "Clubs", 1, 4],
            2: ["Two", "Diamonds", 2, 4],
            3: ["Two", "Hearts", 3, 4],
            4: ["Two", "Spades", 4, 4],
            5: ["Three", "Clubs", 1, 6],
            6: ["Three", "Diamonds", 2, 6],
            7: ["Three", "Hearts", 3, 6],
            8: ["Three", "Spades", 4, 6],
            9: ["Four", "Clubs", 1, 6],
            10: ["Four", "Diamonds", 2, 6],
            11: ["Four", "Hearts", 3, 6],
            12: ["Four", "Spades", 4, 6],
            13: ["Five", "Clubs", 1, 6],
            14: ["Five", "Diamonds", 2, 6],
            15: ["Five", "Hearts", 3, 6],
            16: ["Five", "Spades", 4, 6],
            17: ["Six", "Clubs", 1, 6],
            18: ["Six", "Diamonds", 2, 6],
            19: ["Six", "Hearts", 3, 6],
            20: ["Six", "Spades", 4, 6],
            21: ["Seven", "Clubs", 1, 6],
            22: ["Seven", "Diamonds", 2, 6],
            23: ["Seven", "Hearts", 3, 6],
            24: ["Seven", "Spades", 4, 6],
            25: ["Eight", "Clubs", 1, 6],
            26: ["Eight", "Diamonds", 2, 6],
            27: ["Eight", "Hearts", 3, 6],
            28: ["Eight", "Spades", 4, 6],
            29: ["Nine", "Clubs", 1, 8],
            30: ["Nine", "Diamonds", 2, 8],
            31: ["Nine", "Hearts", 3, 8],
            32: ["Nine", "Spades", 1, 8],
            33: ["Ten", "Clubs", 2, 8], 
            34: ["Ten", "Diamonds", 3, 8],
            35: ["Ten", "Hearts", 4, 8],
            36: ["Ten", "Spades", 1, 8],
            37: ["Jack", "Clubs", 2, 8],
            38: ["Jack", "Diamonds", 2, 8],
            39: ["Jack", "Hearts", 3, 8],
            40: ["Jack", "Spades", 4, 8],
            41: ["Queen", "Clubs", 1, 10],
            42: ["Queen", "Diamonds", 2, 10],
            43: ["Queen", "Hearts", 3, 10],
            44: ["Queen", "Spades", 4, 10],
            45: ["King", "Clubs", 1, 10],
            46: ["King", "Diamonds", 2, 10],
            47: ["King", "Hearts", 3, 10],
            48: ["King", "Spades", 4, 10],
            49: ["Ace", "Clubs", 1, 12],
            50: ["Ace", "Diamonds", 2, 12],
            51: ["Ace", "Hearts", 3, 12],
            52: ["Ace", "Spades", 4, 12],
            53: ["Black", "Joker", 1, 12],
            54: ["Red", "Joker", 1, 12]
        }

if __name__ == "__main__":
    d = Deck()
    while(True):
       print(d.draw().name)
