'''Write a function that uses regular expressions to make sure the password
string it is passed is strong. A strong password is defined as one that is at
least eight characters long, contains both uppercase and lowercase characters,
and has at least one digit. You may need to test the string against multiple
regex patterns to validate its strength.'''

import re

def checkLength(pw):
    if len(pw) < 8:
        return False
    return True

def checkUpperCase(pw):
    uc = re.compile(r'[A-Z]+') # at least 1 uppercase character
    if uc.search(pw):
        return True
    return False

def checkLowerCase(pw):
    lc = re.compile(r'[a-z]+') # at least 1 lowercase character
    if lc.search(pw):
        return True
    return False

def checkDigit(pw):
    digit = re.compile(r'[0-9]+') # at least 1 digit
    if digit.search(pw):
        return True
    return False

# password = input()
password = "Azhl1mn40"

if checkLength(password) & checkUpperCase(password) & checkLowerCase(password) & checkDigit(password):
    print('OK')
else:
    print('Fail')
