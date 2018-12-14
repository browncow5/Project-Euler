'''
Created on Dec 14, 2018

@author: ryand
'''

def sumOfSquaresThroughN(self, n):
    sum = 0
    for x in range(1, n+1):
        sum = sum + x**2
    return sum
        
def squareOfSumsThroughN(self, n):
    sum = 0
    for x in range(1, n+1):
        sum = sum + x    
    return sum**2