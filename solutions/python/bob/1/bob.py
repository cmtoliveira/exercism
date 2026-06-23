def response(hey_bob):
    question = hey_bob.strip().endswith("?")
    upper = hey_bob.isupper()
    if upper == True and question == True:
        return "Calm down, I know what I'm doing!"
    if upper == True:
        return "Whoa, chill out!"
    if question == True:
        return "Sure."
    if hey_bob.isspace() or hey_bob == "":
        return "Fine. Be that way!"
    return "Whatever."