def isValidSSN(string):
    """
    Checks string and returns True if it's a valid
    Social Security Number. Otherwise returns false
    """
    ssnDigits = ""
    if len(string) == 11:
        ssnDigits = string[:3]+string[4:6]+string[7:]
        if ssnDigits.isdigit() and string[3:7:3] == "--":
            return True
    return False


def isPalindrome(string):
    """
    Checks string and returns True if it's a palindrome
    Otherwise returns False
    """
    tmpList = list(string)
    tmpList.reverse()
    backwards = ''.join(tmpList)
    if string == backwards:
        return True
    return False 
    
    
def hasUppercase(string):
    """
    Checks string and returns True if at least one letter
    is uppercase. Otherwise returns False
    """
    for ch in string:
        if ch.isupper():
            return True
    return False

def hasEvenDigit(string):
    """
    Checks string and returns True if at least one character
    is an even number. Otherwise returns False
    """
    for ch in string:
        if ch.isdigit() and int(ch) % 2 == 0:
            return True
    return False

def endsWithS(string):
    """
    Checks string and returns True if it ends with 's' or 'S'
    Otherwise returns False
    """
    if string[-1].lower() == 's':
        return True
    return False

#create empty list for each thing we're checking
ssnLst = []
palinLst = []
upCaseLst = []
evenDigList = []
sList = []

#list for testing purposes
lstOfStrings = ["111-22-3333", "racecar", "Hello", "1111", "12", "121", "racecars", "S"]

for string in lstOfStrings:
    if isValidSSN(string) is True:
        ssnLst.append(string)
    if isPalindrome(string) is True:
        palinLst.append(string)
    if hasUppercase(string) is True:
        upCaseLst.append(string)
    if hasEvenDigit(string) is True:
        evenDigList.append(string)
    if endsWithS(string) is True:
        sList.append(string)

print(ssnLst)
print(ssnLst)
print(palinLst)
print(upCaseLst)
print(evenDigList)
print(sList)
