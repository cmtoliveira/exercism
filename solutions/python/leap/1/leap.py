'''Leap Year'''
def leap_year(year):
    '''A leap year (in the Gregorian calendar) occurs:

    In every year that is evenly divisible by 4.
    Unless the year is evenly divisible by 100, in which case it's only a leap year if the year is also evenly divisible by 400.
    '''
    divisible_by_4 = year%4 == 0
    divisible_by_100 = year%100 == 0
    divisible_by_400 = year%400 == 0

    leap = divisible_by_4 and not divisible_by_100 is True or divisible_by_100 and divisible_by_400 is True
    return leap