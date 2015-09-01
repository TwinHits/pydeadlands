from cards import Deck

class Encounter():
    """An instance of this class is an encounter driven by quickness based
    cards.
        Takes two lists of characters, one for players, one for the marshal
        so that each side has it's own deck.
        Anything else that is a circumstance should be passed in as a keyword
        argument.
        Combat(characters list players, characters list marhsals)
        Possible Keywords:
            surprise=True 
    """
    def __init__(self, players, marshal, **kwargs):
        self.over = False
        self.players = players
        self.marshal = marshal
        self.players_deck = Deck()
        self.marshal_deck = Deck()

        self.surprise = False

        for k in kwargs:
            if k == surprise:
                self.surprise = surprise
        
    def begin(self):
        """Calling this method begins the ecounter. When this method returns,
        the encounter is over."""
        while(self.over == False):
            _round = Round(self)
            while(_round.over == False):
                turns = _round._next()
                print([[t.character.name, t.value] for t in turns]) 
                #The characters take action 
            #check if encounter is over
            self.end()
            self.over = True

    def end(self):
        #destructor actions
        pass

class Round():
    """A round is defined by each character drawing cards and taking
    actions."""
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
        """Takes a list of characters and a deck and returns the cards for those
        characters as a dictionary"""
        for c in characters:
            roll = c.quickness.roll() 

            if roll == 0:
                num_turns = 0
            else:
                num_turns = int(roll/5 + 1)

            cards = [deck.draw() for i in range(0, num_turns)]
            
            #check for black joker

            self.round_cards[c] = cards 

    def _next(self):
        """Calling this method gets the next character in line to start
        combat."""
        #return the next characters to go
        #if there are no more characters to go
        next_turns = []
        turn = self.turns[0] 

        while(len(self.turns) != 0 and self.turns[0].value == turn.value):
            turn = self.turns.pop(0)
            next_turns.append(turn)
    
        if len(self.turns) == 0:
            self.over = True

        return next_turns

class Turn():
    """A single turn in a round. Takes a character and a card. Surfaces the
    card value for easier ordering"""
    def __init__(self, character, card):
        self.character = character
        self.card = card
        self.value = self.card.value
