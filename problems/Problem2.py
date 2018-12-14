'''
Created on Oct 3, 2017

@author: ryand
'''
from utils.Fibonacci import generateFibList

class Problem2(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''

    def run(self):
        print("Running Problem 2:")
        print("\t" + "By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.")

        print("\t" + "Generating Fibonacci as list to a maximum value of four million.")        
        list = generateFibList(self, 4000000)
        
        print("\t" + "Filtering out odd values from Fibonacci list.")
        evenList = []
        for x in list:
            if x%2 == 0:
                evenList.append(x)
        evenFibSum = sum(evenList)        
        print("\t" + "Answer : " + str(evenFibSum))
        return evenFibSum