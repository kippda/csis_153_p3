#Valid SSN

#Palindrome

def hasUppercase(string):
    """
    Checks string and returns True if at least one letter is uppercase
    Otherwise returns False
    """
    for ch in string:
        if ch.isupper():
            return True
    return(False)

#has an even digit

def endsWithS(string):
    """
    Checks string and returns True if it ends with 's' or 'S'
    False
    """
    if string[-1].lower() == 's':
        return(True)
    return(False)


