from cards import Deck

class Encounter():
    """Combat(characters list players, characters list marhsals)
    An instance of this class is an encounter driven by quickness based
    cards drawn turns.
    Takes two lists of characters, one for players, one for the marshal so that each side has it's own deck.
    Anything else that is a circumstance should be passed in as a keyword argument.
    Possible Keywords:
        surprise=True 
    """
    def __init__(self, players, marshal, **kwargs):
        self.over = False
        self.players = players
        self.marshal = marshal
        self.players_deck = Deck()
        self.marshal_deck = Deck()

        #Possible keywords
        self.surprise = False

        #Check for keyword circumstances
        for k in kwargs:
            if k == surprise:
                self.surprise = surprise
        
    def begin(self):
        """Calling begin() begins the ecounter. When this method returns, the encounter is over."""
        while(self.over != True):
            _round = Round(self)
            while(_round.over != True):
                turns = _round._next()
                #TODO The characters take action here
            #TODO Check if encounter is over and then call end()
            self.end()

    def end(self):
        """Calling end() ends the encounter, and performs all end of encounter actions"""
        self.over = True

class Round():
    """A round is defined by each character drawing cards and taking actions until no Turns remain."""
    def __init__(self, encounter):
        self.over = False
        self.encounter = encounter
        self.round_cards = {}
        self.turns = []

        self.__roll_quickness(self.encounter.players, self.encounter.players_deck)
        self.__roll_quickness(self.encounter.marshal, self.encounter.marshal_deck)

        for char in self.encounter.players:
            for card in self.round_cards[char]:
                self.turns.append(Turn(char, card))
                   
        for char in self.encounter.marshal:
            for card in self.round_cards[char]:
                self.turns.append(Turn(char, card))

        self.turns.sort(reverse=True, key=lambda x: x.value)

    def __roll_quickness(self, characters, deck):
        """Takes a list of characters and a deck and adds those cards to that
        character in a dictionary."""
        for c in characters:
            roll = c.quickness.roll() 

            #Check for busts
            if roll == 0:
                num_turns = 0
            else:
                num_turns = int(roll/5 + 1)

            cards = [deck.draw() for i in range(0, num_turns)]
            
            #Check for black joker
            for i in cards:
                if i.name == "Black Joker":
                    i.return_to_deck()
                    if c.sleved_card:
                        c.sleeved_card.return_to_deck()
                        c.sleeved_card = None
                    deck.shuffle()

            self.round_cards[c] = cards 

    def _next(self):
        """Calling this method gets the next character in line to start
        combat, returns two if they are simultanious."""
        next_turns = []
        turn = self.turns[0] 

        while (len(self.turns) != 0 and self.turns[0].value == turn.value):
            turn = self.turns.pop(0)
            next_turns.append(turn)
    
        if len(self.turns) == 0:
            self._end()

        return next_turns

    def _end(self):
        self.over = True
        for c in self.round_cards:
            for t in self.round_cards[c]:
                t.return_to_deck()


class Turn():
    """A struct for a single turn in a round. Takes a character and a card. Surfaces the
    card value for easier ordering"""
    def __init__(self, character, card):
        self.character = character
        self.card = card
        self.value = self.card.value
