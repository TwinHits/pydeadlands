from random import randint

from cards import Deck
from dice import roll_skill

class Trait:
    """Parent stat. Contains holds the aptitude instances that are in it's
    family."""
    def __init__(self, num=1, size=4):
        self.num = num
        self.size = size

    def roll(self, mod=0):
        """Rolls the trait"""
        result = roll_skill(self.num, self.size)
        if result == 0:
            return result
        else:
            return result + mod

    def set_aptitude(self, name, num=0):
        """Adds each aptitude to it's dictionary on character creation, and the
        concentrations that are in it's family."""
        self.__dict__[name] = Aptitude(self, num)

    def set_num(self, num):
        """Set's the number of die for the trait on character creation or
        level up."""
        self.num = num

    def set_size(self, size):
        """Set's the size of die for the trait on character creation or
        level up."""
        self.size = size

class Aptitude:
    def __init__(self, trait, num=0):
        self.num = num
        self.parent = trait 

    def roll(self, mod=0):
        """Roll the skill, returning 0 for a bust"""
        if self.num == 0:
            result = roll_skill(1, self.parent.size)
            return result + mod - 2
        result = roll_skill(self.num, self.parent.size)
        if result == 0:
            return result
        else:
            return result + mod

    def set_concentration(self, name, num=0):
        """Adds each aptitude to it's dictionary on character creation"""
        self.__dict__[name] = Concentration(self, num)

    def set_num(self, num):
        """Set's the number of die for the aptitude on character creation or
        level up."""
        self.num = num

class Concentration:
    def __init__(self, aptitude, num=0):
        self.num = num
        self.parent = aptitude

    def roll(self, mod=0):
        """Roll the skill, returning 0 for a bust, rolling with num=1 if num=0"""
        if self.num == 0:
            result = roll_skill(1, self.parent.size)
            return result - 2
        result = roll_skill(self.num, self.parent.parent.size)
        if result == 0:
            return result
        else:
            return result + mod

    def set_num(self, num):
        """Set's the number of die for the aptitude on character creation or
        level up."""
        self.num = num

class Character:
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
        
    def create_random(self):
        """create a random character based on card draw and random assignment"""
        #Draw cards and get aptitudes
        deck = Deck()
        hand = [deck.draw() for i in range(0,12)]
        traits = [self.__dict__[t] for t in self.__dict__ 
                if type(self.__dict__[t]) is Trait]
       
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

        #Get list of all aptitudes 
        aptitudes = []
        for t in traits:
            for a in t.__dict__:
                if type(t.__dict__[a]) is Aptitude:
                    aptitudes.append(t.__dict__[a])
                    
        #Randomly assign points to aptitudes
        while (aptitude_points > 0):
            if aptitude_points > 5:
                num = int((randint(0,5) + randint(0,5)) / 2)
            else:
                num = aptitude_points
            aptitudes[randint(0, len(aptitudes)-1)].set_num(num)
            aptitude_points -= num

if __name__ == "__main__":
    c = Character() 
    c.create_random()
     
