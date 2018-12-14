'''
Created on Jan 2, 2018

@author: ryand
'''


def isPalindrome(self, number):
    
    possiblePal = str(number)
    possiblePalLenth = len(possiblePal)
    
    if possiblePalLenth == 1:
        return True 
    
    for x in range(0, possiblePalLenth):
        frontIter = x
        backIter = possiblePalLenth - 1 - x
        if possiblePal[frontIter] == possiblePal[backIter]:
            if frontIter == backIter or frontIter == backIter - 1:
#                print(possiblePal + " is a palindrome")
                return True
            else:
                continue
        else:
            return False