from math import sqrt

def score(x, y):
    distance = sqrt((x**2 + y**2))
    if distance > 10:
        return 0
    if 10 >= distance > 5:
        return 1
    if 5 >= distance > 1:
        return 5
    return 10
