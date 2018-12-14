'''
Created on Oct 9, 2017

@author: ryand
'''
from utils.Palindrome import isPalindrome

class Problem4(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def run(self):
        
        print("Running Problem 4")
        print("\t" + "Find the largest palindrome made from the product of two 3-digit numbers.")
        
        largestPal = 1
        largestFactorX = 1
        largestFactorY = 1
        
        listOfPalindromes = []
        
        #This can be improved my reversing the loops to count down
        for x in range(100, 999):
            for y in range(100, 999):
                possiblePal = x*y
                if isPalindrome(self, possiblePal):
                    listOfPalindromes.append(possiblePal)
                    if possiblePal > largestPal:
                        largestPal = possiblePal
                        largestFactorX = x
                        largestFactorY = y

        print ("\t" + "Answer: " + str(largestPal))
        return largestPal