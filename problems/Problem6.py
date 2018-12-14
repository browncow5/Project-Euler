'''
Created on Dec 14, 2018

@author: ryand
'''

from utils import Maths

class Problem6(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.n = 100
        
    def run(self):
        print("Running Problem 6")
        print("\t" + "Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.")
        
        answer = Maths.squareOfSumsThroughN(self, self.n) - Maths.sumOfSquaresThroughN(self, self.n)
        
        print ("\t" + "Answer: " + str(answer))
        
