'''
Created on Oct 4, 2017

@author: ryand
'''
  
import random
        
def filterPrimes(list):
    print(list)
    updatedList = []
    for x in list:
        print("Checking" + str(x))
        if is_probable_prime(x) == False:
#            print(str(x) + " : is NOT prime.")
            list.remove(x)
        else:
            updatedList.append(x)
            print(str(x) + " : is prime")
    return updatedList
           
  #https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Primality_Testing#Python  
"""use Rabin-Miller algorithm to return True (n is probably prime) or False (n is definitely composite)"""    
def is_probable_prime(n, k = 7):
    if n < 6:  # assuming n >= 0 in all cases... shortcut small cases here
        return [False, False, True, True, False, True][n]
    elif n & 1 == 0:  # should be faster than n % 2
        return False
    else:
        s, d = 0, n - 1
        while d & 1 == 0:
            s, d = s + 1, d >> 1
        # Use random.randint(2, n-2) for very large numbers
        for a in random.sample(range(2, min(n - 2, n)), min(n - 4, k)):
            x = pow(a, d, n)
            if x != 1 and x + 1 != n:
                for r in range(1, s):
                    x = pow(x, 2, n)
                    if x == 1:
                        return False  # composite for sure
                    elif x == n - 1:
                        a = 0  # so we know loop didn't continue to end
                        break  # could be strong liar, try another a
                if a:
                    return False  # composite if we reached end of this loop
        return True  # probably prime if reached end of outer looph
    
