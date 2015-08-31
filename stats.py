from dice import roll_skill

class Trait:
    """Parent stat. Contains holds the aptitude instances that are in it's
    family."""
    def __init__(self, num=1, size=4):
        self.num = num
        self.size = size

    def roll(self, mod=0):
        """Rolls the trait
            roll(2) or roll(mod=2) for modifer"""
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
        """Roll the skill, returning 0 for a bust
            roll(2) or roll(mod=2) for modifer"""
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
        self.parent =  aptitude

    def roll(self, mod=0):
        """Roll the skill, returning 0 for a bust
            roll(2) or roll(mod=2) for modifer"""
        if self.num == 0:
            result = roll_skill(1, self.parent.parent.size)
            return result + mod - 2
        result = roll_skill(self.num, self.parent.parent.size)
        if result == 0:
            return result
        else:
            return result + mod

    def set_num(self, num):
        """Set's the number of die for Concentration on character creation or
        level up."""
        self.num = num
