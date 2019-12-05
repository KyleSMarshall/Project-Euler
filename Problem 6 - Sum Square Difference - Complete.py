'''
- Problem 6 -
Sum Square Difference


The sum of the squares of the first ten natural numbers is,
1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten 
natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first 
one hundred natural numbers and the square of the sum.

'''

def Square_Sum_Dif(n):
    # n is the upper limit of numbers
    
    sum_squares = 0
    sum_numbers = 0
    for i in range (1, n+1):
        square = i**2
        sum_squares = sum_squares + square
        sum_numbers = sum_numbers + i
    square_sum = sum_numbers**2
    difference = square_sum - sum_squares
    return difference

#%%
import time

ti = time.time()
print(str(Square_Sum_Dif(100)))
tf = time.time()
t = tf-ti
print('%.2f' % t + ' ::================:: Time for the first 100 numbers ')
