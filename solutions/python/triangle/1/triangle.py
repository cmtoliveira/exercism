'''Determine if a triangle is equilateral, isosceles, or scalene.'''

def equilateral(sides):
    '''Checks if it is an equilateral triangle given a list with 3 values
    An equilateral triangle has all three sides the same length.
    '''
    a = sides[0]
    b = sides[1]
    c = sides[2]
    triangle = (a+b >= c and b+c >= a and a+c >=b) is True and (a > 0 and b > 0 and c > 0) is True
    if triangle is False:
        return False
    return a == b == c
    
def scalene(sides):
    '''Checks if it a scalene triangle given a list with 3 values
    A scalene triangle has all sides of different lengths.
    '''
    a = sides[0]
    b = sides[1]
    c = sides[2]
    triangle = (a+b >= c and b+c >= a and a+c >=b) is True and (a > 0 and b > 0 and c > 0) is True
    if triangle is False:
        return False
    return a != b and b != c and a != c

def isosceles(sides):
    '''Checks if it is an isosceles triangle by checking if it is not a scalene triangle given a list with 3 values
    An isosceles triangle has at least two sides the same length. (It is sometimes specified as having exactly two sides the same         length, but for the purposes of this exercise we'll say at least two.)
    '''
    a = sides[0]
    b = sides[1]
    c = sides[2]
    triangle = (a+b >= c and b+c >= a and a+c >=b) is True and (a > 0 and b > 0 and c > 0) is True
    if triangle is False:
        return False
    return scalene(sides) is False

