'''
Created on Oct 2, 2017

@author: ryand
'''

class Problem1(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.limit = 1000
        self.sum = 0
        
    def run(self):
        
        print("Running Problem 1")
        print("\t" + "Find the sum of all the multiples of 3 or 5 below 1000.")
        
        for x in range(1, self.limit):
            if (x%3 == 0 or x%5 == 0):
                self.sum += x
        
        print ("\t" + "Answer: " + str(self.sum))
        return self.sum