'''Raindrops
Your task is to convert a number into its corresponding raindrop sounds.
'''
def convert(number):
    '''If a given number (int):
    is divisible by 3, add "Pling" to the result.
    is divisible by 5, add "Plang" to the result.
    is divisible by 7, add "Plong" to the result.
    is not divisible by 3, 5, or 7, the result should be the number as a string.

    Returns the sound (str) based on a given number (int)
    '''
    divisible_by_3 = number%3 == 0
    divisible_by_5 = number%5 == 0
    divisible_by_7 = number%7 == 0
    sound = ''
    
    if divisible_by_3:
        sound += 'Pling'
    if divisible_by_5:
        sound += 'Plang'
    if divisible_by_7:
        sound += 'Plong'
    if not (divisible_by_3 or divisible_by_5 or divisible_by_7):
        sound = str(number)
    return sound 
