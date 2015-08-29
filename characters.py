from dice import roll_skill

class Attribute:
    """Parent stat. Contains holds the trait instances that are in it's
    family."""
    def __init__(self, num=1, size=4):
        self.num = num
        self.size = size

    def roll(self, mod=0):
        """Rolls the attribute"""
        result = roll_skill(self.num, self.size)
        if result == 0:
            return result
        else:
            return result + mod

    def set_trait(self, name, num=0):
        """Adds each trait to it's dictionary on character creation"""
        self.__dict__[name] = Trait(self, num)

    def set_num(num):
        """Set's the number of die for the attribute on character creation or
        level up."""
        self.num = num

    def set_size(size):
        """Set's the sizr of die for the attribute on character creation or
        level up."""
        self.size = size

class Trait:
    def __init__(self, attribute, num=0):
        self.num = num
        self.parent = attribute 

    def roll(self, mod=0):
        """Roll the skill, returning 0 for a bust"""
        result = roll_skill(self.num, self.parent.size)
        if result == 0:
            return result
        elif self.num == 0:
            return result - 2
        else:
            return result + mod

    def set_concentration(self, name, num=0):
        """Adds each trait to it's dictionary on character creation"""
        self.__dict__[name] = Concentration(self, num)

    def set_num(num):
        """Set's the number of die for the trait on character creation or
        level up."""
        self.num = num

class Concentration:
    def __init__(self, trait, num=0):
        self.num = num
        self.parent = trait

    def roll(self, mod=0):
        result = roll_skill(self.num, self.parent.parent.size)
        if result == 0:
            return result
        elif self.num == 0:
            return result - 2
        else:
            return result + mod

    def set_num(num):
        """Set's the number of die for the trait on character creation or
        level up."""
        self.num = num

class Character:
    def __init__(self):
        """Any deadlands character, player, npc, or monster. Generates
        attributes and traits instances on initialization.""" 
        self.cognition = Attribute()
        self.cognition.set_trait("artillery")
        self.cognition.set_trait("arts")
        self.cognition.set_trait("scrutinize")
        self.cognition.set_trait("search", 1)
        self.cognition.set_trait("tracking")
        self.knowledge = Attribute()
        self.knowledge.set_trait("academia")
        self.knowledge.set_trait("areaknowledge")
        self.knowledge.areaknowledge.set_concentration("homecountry", 2)
        self.knowledge.set_trait("demolition")
        self.knowledge.set_trait("disguise")
        self.knowledge.set_trait("language")
        self.knowledge.language.set_concentration("nativetongue")
        self.knowledge.set_trait("medicine")
        self.knowledge.set_trait("professional")
        self.knowledge.set_trait("science")
        self.knowledge.set_trait("trade")
        self.mein = Attribute()
        self.mein.set_trait("animalhandling")
        self.mein.set_trait("leadership")
        self.mein.set_trait("overawe")
        self.mein.set_trait("performin")
        self.mein.set_trait("persuasion")
        self.mein.set_trait("taletellin")
        self.smarts = Attribute()
        self.smarts.set_trait("bluff")
        self.smarts.set_trait("gambling")
        self.smarts.set_trait("ridicule")
        self.smarts.set_trait("scroungin")
        self.smarts.set_trait("survival")
        self.smarts.set_trait("streetwise")
        self.smarts.set_trait("tinkerin")
        self.spirit = Attribute()
        self.spirit.set_trait("faith")
        self.spirit.set_trait("guts")
        self.deftness = Attribute()
        self.deftness.set_trait("bow")
        self.deftness.set_trait("filchin")
        self.deftness.set_trait("lockpickin")
        self.deftness.set_trait("sleightohand")
        self.deftness.set_trait("speedload")
        self.deftness.set_trait("throwin")
        self.nimbleness = Attribute()
        self.deftness.set_trait("climbin", 1)
        self.deftness.set_trait("dodge")
        self.deftness.set_trait("drivin")
        self.deftness.set_trait("fightin")
        self.deftness.set_trait("ridin")
        self.deftness.set_trait("sneak", 1)
        self.deftness.set_trait("swimming")
        self.deftness.set_trait("teamster")
        self.strength = Attribute()
        self.quickness = Attribute()
        self.quickness.set_trait("speeddraw")
        self.vigor = Attribute()

        self.pace = 0
        self.size = 5
        
    #def generate:
        """create a random character based on card draw and random assignment"""
    
if __name__ == "__main__":
    c = Character()
    print(c.knowledge.roll())
