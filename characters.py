from random import randint

from cards import Deck
from stats import Aptitude, Trait, Concentration

class Character:
    def create_random(self):
        """create a random character based on card draw and random assignment"""
        #Get list of traits and aptitudes
        traits, aptitudes = self.__get_stats()

        #Draw cards and get aptitudes
        deck = Deck()
        hand = [deck.draw() for i in range(0,12)]
       
        #Convert jokers to dice size and check for Mysterious Past
        for c in hand:
            if c.suit == "Joker":
               self.mysterious_past = True
               card = deck.draw()
               c.suit = card.suit
               
        #Remove two lowest value cards
        hand.remove(min(hand, key=lambda x: x.value))
        hand.remove(min(hand, key=lambda x: x.value))

        #Apply num and size randomly to aptitudes
        for t in traits:
            c = hand.pop()
            t.set_num(c.die_num)
            t.set_size(c.die_size)

        #Math out secondary attributes
        self.pace = self.quickness.size
        self.wind = self.vigor.size + self.spirit.size

        #Get aptitude points
        aptitude_points = self.knowledge.size + self.smarts.size + self.cognition.size

        #Randomly assign points to aptitudes
        while (aptitude_points > 0):
            if aptitude_points > 5:
                num = int((randint(0,5) + randint(0,5)) / 2)
            else:
                num = aptitude_points
            aptitudes[randint(0, len(aptitudes)-1)].set_num(num)
            aptitude_points -= num

    def __get_stats(self):
        """Returns characters stats to display to the user. Returns tuple of
        traits and aptitudes"""
        #Get list of all traits
        traits = [self.__dict__[t] for t in self.__dict__ 
                if type(self.__dict__[t]) is Trait]

        #Get list of all aptitudes 
        aptitudes = []
        for t in traits:
            for a in t.__dict__:
                if type(t.__dict__[a]) is Aptitude:
                    aptitudes.append(t.__dict__[a])
        
        return (traits, aptitudes)
        
    def __init__(self):
        """Any deadlands character, player, npc, or monster. Generates
        traits and aptitudes instances on initialization.""" 
        self.cognition = Trait()
        self.cognition.set_aptitude("artillery")
        self.cognition.set_aptitude("arts")
        self.cognition.set_aptitude("scrutinize")
        self.cognition.set_aptitude("search", 1)
        self.cognition.set_aptitude("tracking")
        self.knowledge = Trait()
        self.knowledge.set_aptitude("academia")
        self.knowledge.set_aptitude("areaknowledge")
        self.knowledge.areaknowledge.set_concentration("homecountry", 2)
        self.knowledge.set_aptitude("demolition")
        self.knowledge.set_aptitude("disguise")
        self.knowledge.set_aptitude("language")
        self.knowledge.language.set_concentration("nativetongue", 2)
        self.knowledge.set_aptitude("medicine")
        self.knowledge.set_aptitude("professional")
        self.knowledge.set_aptitude("science")
        self.knowledge.set_aptitude("trade")
        self.mein = Trait()
        self.mein.set_aptitude("animalhandling")
        self.mein.set_aptitude("leadership")
        self.mein.set_aptitude("overawe")
        self.mein.set_aptitude("performin")
        self.mein.set_aptitude("persuasion")
        self.mein.set_aptitude("taletellin")
        self.smarts = Trait()
        self.smarts.set_aptitude("bluff")
        self.smarts.set_aptitude("gambling")
        self.smarts.set_aptitude("ridicule")
        self.smarts.set_aptitude("scroungin")
        self.smarts.set_aptitude("survival")
        self.smarts.set_aptitude("streetwise")
        self.smarts.set_aptitude("tinkerin")
        self.spirit = Trait()
        self.spirit.set_aptitude("faith")
        self.spirit.set_aptitude("guts")
        self.deftness = Trait()
        self.deftness.set_aptitude("bow")
        self.deftness.set_aptitude("filchin")
        self.deftness.set_aptitude("lockpickin")
        self.deftness.set_aptitude("sleightohand")
        self.deftness.set_aptitude("speedload")
        self.deftness.set_aptitude("throwin")
        self.nimbleness = Trait()
        self.nimbleness.set_aptitude("climbin", 1)
        self.nimbleness.set_aptitude("dodge")
        self.nimbleness.set_aptitude("drivin")
        self.nimbleness.set_aptitude("fightin")
        self.nimbleness.set_aptitude("ridin")
        self.nimbleness.set_aptitude("sneak", 1)
        self.nimbleness.set_aptitude("swimming")
        self.nimbleness.set_aptitude("teamster")
        self.strength = Trait()
        self.quickness = Trait()
        self.quickness.set_aptitude("speeddraw")
        self.vigor = Trait()

        self.pace = 0
        self.size = 5
        self.wind = 0
        mysterious_past = False
