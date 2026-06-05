'''
Calculate the number of grains of wheat on a chessboard.

A chessboard has 64 squares. Square 1 has one grain, square 2 has two grains, square 3 has four grains, and so on, doubling each time.

Write code that calculates:

    the number of grains on a given square
    the total number of grains on the chessboard
'''

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
    square_value = 2**(number-1)
    return square_value

def total():
    '''Returns the total value of grains on the board'''
    total_value = 0    
    for square_number in range(1,65):
        total_value += 2**(square_number-1)   

    return total_value
