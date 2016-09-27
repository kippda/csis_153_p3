"""
Takes input from argv and checks if any of the strings are
a valid social security number, are a palindrome, if they have
an uppercase letter, if they have an even digit and if they
end with 's' or 'S'. At the end, prints a label and a list
containing each string that meets the corresponding test
"""
__author__ = "Dane Kipp"
__date__ = "2016-09-26"

import sys

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
    if string.lower() == backwards.lower():
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
def main():
    #list for testing purposes
    #tmpStr = ["111-22-3333", "RacEcar", "Hello", "1111", "12", "121", "racecars", "S"]

    if len(sys.argv) < 2:
        print("Error: No input provided")
    else:
        tmpStr = sys.argv[1:]

        ssnLst = []
        palinLst = []
        upCaseLst = []
        evenDigLst = []
        sLst = []
        
        #check tmpStr to see if any strings meet the various parameters
        for string in tmpStr:
            if isValidSSN(string) is True:
                ssnLst.append(string)
            if isPalindrome(string) is True:
                palinLst.append(string)
            if hasUppercase(string) is True:
                upCaseLst.append(string)
            if hasEvenDigit(string) is True:
                evenDigLst.append(string)
            if endsWithS(string) is True:
                sLst.append(string)

        #print the results of the testing
        print('{:25s}'.format("Valid SSNs:"), ssnLst)
        print('{:25s}'.format("Palindromes:"), palinLst)
        print('{:25s}'.format("At least one Uppercase:"), upCaseLst)
        print('{:25s}'.format("At least one even digit:"), evenDigLst)
        print('{:25s}'.format("Ends with 's' or 'S':"), sLst)

if __name__ == "__main__":
    main()
