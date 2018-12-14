'''
Created on Oct 3, 2017

@author: ryand
'''




        
def generateFibList(self, limit):
    fibList = [1, 2]
    nextFib = 0
    
    while(True):
        nextFib = fibList[-1] + fibList[-2]
        if (nextFib < limit):
            fibList.append(nextFib)
        else:
            break
    return fibList    
    
        
