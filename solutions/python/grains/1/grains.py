def square(number):
    '''
    Select a square number between 1 and 64 to see how many grains are on this square. The quantity begins at 1 and doubles on the        next square
    Parameter:
        number(int): The number of the chosen square. 1 <= number <= 64
    Returns:
        The number of grains on a given square based on the square number
    '''
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    square = 2**(number-1)
    return square

def total():
    total = 0    
    for i in range(1,65):
        total += 2**(i-1)   

    return total
