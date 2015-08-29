from random import randint

def roll(num, size):
    """Location"""
    results = 0
    for i in range(0, num):
        results += randint(1, size)
    return results

def roll_damage(num, size):
    """Damage"""
    results = 0 
    for i in range(0, num):
        r = roll(1, size)
        while r == size:
            results += r
            r = roll(1, size)
        results += r
    return results

def roll_skill(num, size):
    """Skills"""
    results = 0 
    busts = 0
    for i in range(0, num):
        r = roll(1, size)
        if r == 1:
            busts += 1
        else:
            while (r == size):
                results += r
                r = roll(1, size)
        results += r
    if busts >= num/2:
        return 0
    return results

def roll_wind(num, size):
    """Wind"""
    results = 0 
    for i in range(0, num):
        r = roll(1, size)
        while (r == size):
            results += r
            r = roll(1, size)
        if r > results:
            results = r
    return results
