'''
Created on Oct 4, 2017

@author: ryand
'''

from utils import Primes


def getFactorsAsList(number):
    listOfFactors = []
    limit = int(number/2)
    for x in range(1, limit):
        if number%x == 0:
            listOfFactors.append(x)
            
    return listOfFactors

def getPrimeFactorsAsListFromTree(number):
    currentNumber = number
    listOfPrimeFactors = []
    limit = number**0.5
    x = 2
    
    #this is the wrong limit
    while(x <= currentNumber):
        if (currentNumber%x == 0):
            currentNumber = currentNumber/x
            listOfPrimeFactors.append(x)
            
        else:
            x+=1

    return listOfPrimeFactors

def getSmallestPrimeFactorFromTree(number):
    currentNumber = number
    x = 2
    
    while(x <= currentNumber):
        if (currentNumber%x == 0):
            currentNumber = currentNumber/x
            return x
        else:
            x+=1
    return -1

def getSmallestPrimeFactor(number):
    smallestPrimeFactor = -1
    if (number % 2 == 0):
        smallestPrimeFactor = 2
        return smallestPrimeFactor
    else:
        listOfPrimeFactors = getPrimeFactorsAsListFromTree(number)

        smpf = listOfPrimeFactors[0]
        
        return smpf
