from dice import roll_skill

class Attribute:
    def __init__(self, num=1, size=4):
        self.num = num
        self.size = size

    def roll(self, mod=0):
        result = roll_skill(self.num, self.size)
        if result == 0:
            return result
        else:
            return result + mod

    def add_trait(self, name, num):
        self.__dict__[name] = Trait(self, attribute, num)

    def set_num(num):
        self.num = num

    def set_size(size):
        self.size = size

class Trait:
    def __init__(self, attribute, num=0):
        self.num = num
        self.parent = attribute 

    def roll(self, mod=0):
        result = roll_skill(self.num, self.parent.size)
        if result == 0:
            return result
        elif self.num == 0:
            return result - 2
        else:
            return result + mod

class Character:
    def __init__(self):
        """Set up traits, attributes, and general stats"""
        self.cognition = Attribute()
        self.knowledge = Attribute()
        self.mein = Attribute()
        self.smarts = Attribute()
        self.spirit = Attribute()
        self.deftness = Attribute()
        self.nimbleness = Attribute()
        self.strength = Attribute()
        self.quickness = Attribute()
        self.vigor = Attribute()
        
    #def generate:
        """create a random character based on card draw and random assignment"""
    
if __name__ == "__main__":
    c = Character()
    print(c.cognition.roll())
