from random import randint, shuffle

card_lookup_table = {
            1: ["Black", "Joker"],
            2: ["Two", "Clubs"],
            3: ["Two", "Diamonds"],
            4: ["Two", "Hearts"],
            5: ["Two", "Spades"],
            6: ["Three", "Clubs"],
            7: ["Three", "Diamonds"],
            8: ["Three", "Hearts"],
            9: ["Three", "Spades"],
            10: ["Four", "Clubs"],
            11: ["Four", "Diamonds"],
            12: ["Four", "Hearts"],
            13: ["Four", "Spades"],
            14: ["Five", "Clubs"],
            15: ["Five", "Diamonds"],
            16: ["Five", "Hearts"],
            17: ["Five", "Spades"],
            18: ["Six", "Clubs"],
            19: ["Six", "Diamonds"],
            20: ["Six", "Hearts"],
            21: ["Six", "Spades"],
            22: ["Seven", "Clubs"],
            23: ["Seven", "Diamonds"],
            24: ["Seven", "Hearts"],
            25: ["Seven", "Spades"],
            26: ["Eight", "Clubs"],
            27: ["Eight", "Diamonds"],
            28: ["Eight", "Hearts"],
            29: ["Eight", "Spades"],
            30: ["Nine", "Clubs"],
            31: ["Nine", "Diamonds"],
            32: ["Nine", "Hearts"],
            33: ["Nine", "Spades"],
            34: ["Ten", "Clubs"], 
            35: ["Ten", "Diamonds"],
            36: ["Ten", "Hearts"],
            37: ["Ten", "Spades"],
            38: ["Jack", "Clubs"],
            39: ["Jack", "Diamonds"],
            40: ["Jack", "Hearts"],
            41: ["Jack", "Spades"],
            42: ["Queen", "Clubs"],
            43: ["Queen", "Diamonds"],
            44: ["Queen", "Hearts"],
            45: ["Queen", "Spades"],
            46: ["King", "Clubs"],
            47: ["King", "Diamonds"],
            48: ["King", "Hearts"],
            49: ["King", "Spades"],
            50: ["Ace", "Clubs"],
            51: ["Ace", "Diamonds"],
            52: ["Ace", "Hearts"],
            53: ["Ace", "Spades"],
            54: ["Red", "Joker"]
        }

class Card:
    """A card is really just a number"""
    def __init__(self, value):
        self.value = value
        self.number = card_lookup_table[self.value][0]
        self.suit = card_lookup_table[self.value][1]
        if self.value == 1 or self.value == 54:
            self.name = self.number + " " + self.suit
        else:
            self.name = self.number + " of " + self.suit

class Deck:
    """A set of 54 cards"""
    def __init__(self):
        self.cards = [Card(i) for i in range(1, 55)]
       self.shuffle()

    def draw(self):
        return self.cards.pop()

    def shuffle(self):
        return self.cards.shuffle()

if __name__ == "__main__":
    d = Deck()
    print(d.draw())
    print(len(d.cards))
