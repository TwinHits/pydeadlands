from dice import roll_skill

class Trait:
    def __init__(self, num, size):
        self.num = num
        self.size = size

    def roll(self, mod=0):
        result = roll_skill(self.num, self.size)
        if result == 0:
            return result
        else if num == 0:
            return result - 2
        else:
            return result + mod

class Attribute:
    def __init__(self, num, size):
        self.num = num
        self.size = size

    def roll(self, mod=0):
        result = roll_skill(self.num, self.size)
        if result == 0:
            return result
        else:
            return result + mod

    def add_trait(self, name, num):
        self.__dict__[name] = Trait(num, self.size)
        
class Character:
    def generate:
        """create a random character based on card draw and random assignment"""
        #pass

    def create:
        """create a random character based on card draw and manual assignment"""
        pass
