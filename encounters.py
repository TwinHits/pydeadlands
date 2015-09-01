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

    def __init__(players, marshals, **kwargs):
        self.over = False
        self.players = players
        self.marshals = marshals
        self.players_deck = Deck()
        self.marshals_deck = Deck()

        self.surprise = False

        for k in kwargs:
            if k == surprise:
                self.surprise = surprise

        
    def begin():
        """Calling this method begins the ecounter. When this method returns,
        the encounter is over."""
        while(!self.over):
            _round = Round()
            while(!_round.over):
                #The characters take action 
                _round._next()
                

    class Round():
        def __init__():
            self.over == False
            #Do the card drawing and turn organizing
        
        def _next():
            """Calling this method gets the next character in line to start
            combat."""
            #return the next character to go


if __name__ == "__main__":
    pass
