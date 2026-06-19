def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    check = ""
    for letter in alphabet:
        if letter in sentence.lower():
            check += letter
    return alphabet == check
        
    
