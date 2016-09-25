#Valid SSN

#Palindrome

def hasUppercase(string):
    """
    Checks string and returns True if at least one letter
    is uppercase. Otherwise returns False
    """
    for ch in string:
        if ch.isupper():
            return True
    return(False)

def hasEvenDigit(string):
    """
    Checks string and returns True if at least one character
    is an even number. Otherwise returns False
    """
    for ch in string:
        if ch.isdigit() and int(ch) % 2 == 0:
            return(True)
    return(False)

def endsWithS(string):
    """
    Checks string and returns True if it ends with 's' or 'S'
    Otherwise returns False
    """
    if string[-1].lower() == 's':
        return(True)
    return(False)


