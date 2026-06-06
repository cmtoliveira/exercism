'''Raindrops
Your task is to convert a number into its corresponding raindrop sounds.

If a given number:

    is divisible by 3, add "Pling" to the result.
    is divisible by 5, add "Plang" to the result.
    is divisible by 7, add "Plong" to the result.
    is not divisible by 3, 5, or 7, the result should be the number as a string.
'''
def convert(number):
    divisible_by_3 = number%3 == 0
    divisible_by_5 = number%5 == 0
    divisible_by_7 = number%7 == 0
    sound = ""
    
    if divisible_by_3:
        sound = sound + 'Pling'
    if divisible_by_5:
        sound = sound + 'Plang'
    if divisible_by_7:
        sound = sound + 'Plong'
    if not (divisible_by_3 or divisible_by_5 or divisible_by_7):
        sound = str(number)
    return sound 
