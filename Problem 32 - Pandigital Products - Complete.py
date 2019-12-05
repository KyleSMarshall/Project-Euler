'''
- Problem 32 - 
Pandigital Products

We shall say that an n-digit number is pandigital if it makes use of all 
the digits 1 to n exactly once; for example, the 5-digit number, 15234, 
is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing 
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity 
can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
'''
import itertools
import numpy as np

def Pandigital():
    pandigital_products = []
    for multiplicand in itertools.count(10):
        for multiplier in itertools.count(2):
            product = multiplicand * multiplier
            multiplicand_str = str(multiplicand)
            multiplier_str = str(multiplier)
            product_str = str(product)
            digits = list(multiplicand_str + multiplier_str + product_str)
            digits.sort()
            if len(digits) == 9:
                for value in range(1, 10):
                    if digits[value-1] != str(value):
                        break
                else:
                    pandigital_products.append(int(product))
                    break
            elif len(digits) > 9:
                break
        if multiplicand == 5000:
            break
    # Get sum of unique products
    pandigital_products_sum = np.sum(np.unique(pandigital_products))
    return pandigital_products_sum
    
        

#%%
Pandigital()
            
                
            
