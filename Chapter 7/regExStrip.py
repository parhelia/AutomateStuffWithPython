''' Create a RegEx version of strip() that removes white space at the beginning
and end
'''
import re

def myStrip(aStr):
    reg = re.compile(r'^\s*(.*?)\s*$', re.DOTALL)
    return reg.sub(r'\1', aStr)

def myTest(aStr):
    if myStrip(aStr) == aStr.strip():
        print True
    else:
        print 'Fail'

# Unit test

myTest('    one 123          \t   xyz \n ABC   ')
myTest(' one 123 \t xyz \n ABC \n \t')
myTest('      one 123          ')
myTest(' \t   one 123')
myTest('one 123 \t  ')
