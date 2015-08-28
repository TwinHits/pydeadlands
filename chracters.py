from dice import roll_skill

class Trait:
    num = 1
    size = 4

    def __init__(self, num, size):
        self.num = num
        self.size = size

    def roll(self, mod=0):
        result = roll_skill(self.num, self.size)
        if result == 0:
            print("Bust!")
            return result
        else:
            return print(result + mod)

if __name__ == "__main__":
    cognition = Trait(3, 6)
    cognition.roll()
