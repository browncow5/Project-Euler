'''
Created on Oct 4, 2017

@author: ryand
'''
from utils import Factors, Primes

class Problem3(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
    def run(self):
        print("Running Problem 3")
        print("\t" + "What is the largest prime factor of the number 600851475143 ?")
        
        print("\t" + "Getting prime factors of 600851475143 as list using prime factor tree.")
        listOfFactors = Factors.getPrimeFactorsAsListFromTree(600851475143)        
        print("\t" + "List of all factors")
        maximumPrimeFactor = max(listOfFactors)
        
        print("\t" + "Answer : " + str(maximumPrimeFactor))