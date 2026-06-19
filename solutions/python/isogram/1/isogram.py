'''Isogram'''

def is_isogram(string):
    '''Determine if a word or phrase is an isogram. An isogram (also known as a "non-pattern word") is a word or phrase without a         repeating letter, however spaces and hyphens are allowed to appear multiple times.
    '''
    exceptions = " -"
    i = 0
    for letter in string.lower():
        i += 1
        if letter in string.lower()[i::]:
            if letter in exceptions:
                continue
            return False
    return True 
