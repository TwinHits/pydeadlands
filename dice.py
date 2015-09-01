from random import randint

def roll(num, size):
    """Returns the cumulative total of num rolls of die size. A regular dnd
    roll, and a location roll."""

    results = 0

    for i in range(0, num):
        results += randint(1, size)

    return results


def roll_damage(num, size):
    """Returns the cumulative total of num rolls of die size with raises. A
    damage roll."""

    results = 0 

    for i in range(0, num):
        r = roll(num, size)
        while r == size:
            results += r
            r = roll(1, size)
        results += r

    return results


def roll_skill(num, size):
    """Returns the highest roll of num rolls of die size with raises and bust
    checking. Bust will return 0. A skill roll."""

    results = []
    busts = 0
    result = 0

    for i in range(0, num):
        r = roll(1, size)
        if r == 1:
            busts += 1
            result = r
        elif r == size:
            while (r == size):
                result += r
                r = roll(1, size)
        else:
            result = r
        results.append(result)

    if busts >= num/2:
        return 0
    else:
        return max(results)


def roll_wind(num, size):
    """Returns the highest roll of num rolls of die size with raises. A wind
    roll."""

    results = []
    result = 0

    for i in range(0, num):
        r = roll(1, size)
        if r == size:
            while (r == size):
                result += r
                r = roll(1, size)
        else:
            result = r
        results.append(result)

    else:
        return max(results)
