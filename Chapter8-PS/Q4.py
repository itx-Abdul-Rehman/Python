# write a function to print first n lines of the following pattern
# ***
# **
# *


def printPattern(n):
    if(n==0):
        return
    
    print('*'*n)
    return printPattern(n-1)
    
n=int(input('Enter n (to print pattern):'))

printPattern(n)