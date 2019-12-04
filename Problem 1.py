
' - PROBLEM - '
'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

import numpy as np

def Multiples_3_5(x):
    
    multiples = []
    
    for i in range(0, x):
        if (i%3 == 0) or (i%5 == 0):
            multiples.append(i)
    
    multiples_sum = np.sum(multiples)

    return multiples_sum
            
#%%
# Call function
Multiples_3_5(1000)