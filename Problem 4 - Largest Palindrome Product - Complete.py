'''
- Problem 4 -
Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome 
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

import numpy as np

def Palindrome(start, stop):
    # n is upper limit
    pal_products = []
    for i in range(start, stop):
        for j in range(start, stop):
            product = i*j
            product_check = list(str(product))
            for number in range(0, len(product_check)):
                if product_check[number] != product_check[-1-number]:
                    # Not a palindrome
                    break
            else:
                pal_products.append(product)
    max_pal = np.max(pal_products)
    return max_pal
#%%
Palindrome(100, 1000)
# result is 906609
