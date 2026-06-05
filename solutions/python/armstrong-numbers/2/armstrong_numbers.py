'''Armstrong Number'''
def is_armstrong_number(number):
    '''An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.
    Receive a number and checks if it is an Armstrong number
    Parameter: number(int)
    Returns: bool
    '''
    digit_list = [int(digit) for digit in str(number)]
    total = 0
    for digit in digit_list:
        total += digit**len(digit_list)
    it_is = total == number
    return it_is