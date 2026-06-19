def is_pangram(sentence):
    '''Function that tests if a sentence is a pangram. A pangram is a sentence using every letter of the alphabet at least once.
    Receives sentence (str) and returns a boolean
    '''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    check = ""
    for letter in alphabet:
        if letter in sentence.lower():
            check += letter
    return alphabet == check
        
    
