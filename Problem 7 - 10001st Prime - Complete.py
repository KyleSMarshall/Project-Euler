'''
- Problem 7 -
10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.

What is the 10001st prime number?
'''

''' 
Returns the 10001th prime number in 6.92 seconds.  Ans = 104743
'''

import numpy as np
import itertools

def Prime_Gen(n):
    # Generates the n'th prime number
    start = 3
    primes = [2]
    for i in range (2, n+1):
        for j in itertools.count(start, 2):
            for k in primes: 
            # Big save - we only need to iterate over previous primes    
                if j%k == 0:
                    # Not a prime
                    break
            else:
                # Is a prime
                primes.append(j)
                start = j + 2
                break
            
    return primes[-1]


#%%
import time

ti = time.time()
print(str(Prime_Gen(10001)))
tf = time.time()
t = tf-ti
print('%.2f' % t + ' ::================:: Time for the 10001th digit')

        
        
        
