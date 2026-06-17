def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    factor = 1
    i = number//2
    while i > 1:
        if number%i == 0:
            factor += i
        i -= 1
    if factor < number or factor == 1:
        return "deficient"
    if factor == number:
        return "perfect"
    if factor > number:
        return "abundant"
