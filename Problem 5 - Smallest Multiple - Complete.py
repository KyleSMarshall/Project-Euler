'''
- Problem 5 -
Smallest Multiple

2520 is the smallest number that can be divided by each of 
the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible 
by all of the numbers from 1 to 20?

'''

def Smallest_Multiple(n):
    # n is the upper limit on the range for the dividends
    smallest_multiple = False
    number = 10 # The starting point for checking for multiples
    while smallest_multiple == False:
        for i in range(1, n+1):
            if number%i != 0:
                # Not a multiple
                break
        else:
            multiple = number
            smallest_multiple = True
            
        number = number + 2 # Increment for next loop
    return multiple

#%%
Smallest_Multiple(20)
# Ans is 232792560
