'''Collatz Conjecture'''
def steps(number):
    '''
    Given a positive integer, return the number of steps it takes to reach 1 according to the rules of the Collatz Conjecture.
    The rules were deceptively simple. Pick any positive integer.

        If it's even, divide it by 2.
        If it's odd, multiply it by 3 and add 1.
    '''
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    step_counter = 0
    while number != 1:
        step_counter += 1
        if number%2 == 0: 
            number = number/2
        else: number = number*3 + 1
    return step_counter
            
        
