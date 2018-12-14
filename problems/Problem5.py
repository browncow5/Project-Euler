'''
Created on Dec 14, 2018

@author: ryand
'''
from time import sleep
import unittest

class Problem5(object):
    '''
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    '''


    def __init__(self):
        '''
        Constructor
        '''
                
    def run(self):
        print("Running Problem 5")
        print("\tWhat is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?")
        
        # Expected = 232792560
        
        answer = Problem5.findSmallestMultiple(self, 20)
        print("\t" + "Answer : " + str(answer))
        
    def findSmallestMultiple(self, limitParm):
        
        smallestNumber = limitParm + 1
        while True:
            #print("Trying : " + str(smallestNumber))
            #sleep(0.005)
            for x in range(2, limitParm + 1):
                #print(str(smallestNumber) + " : " + str(x))
                if (smallestNumber%x != 0):
                    #print("Break on x =" + str(x))
                    smallestNumber = smallestNumber +1
                    break
                #print (str(x) + " : " + str(smallestNumber))
                #print("Limit Parm : " + str(limitParm) + " : " + str(x))
                if (x == limitParm):
                    #print("Smallest =" + str(smallestNumber))
                    return smallestNumber
                
            
            
