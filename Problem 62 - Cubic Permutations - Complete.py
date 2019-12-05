'''
- Problem 62 -
Cubic Permutations 

The cube, 41063625 (345**3), can be permuted to produce two other 
cubes: 56623104 (384**3) and 66430125 (405**3). In fact, 41063625 is 
the smallest cube which has exactly three permutations of its digits 
which are also cube.

Find the smallest cube for which exactly five permutations of its 
digits are cube.
'''
import itertools
import numpy as np

def Cubic_Permutations(n):
    '''
    Generate all cubic numbers in a for loop, then sort the number. If the
    sorted number is already contained within the cube_data dict, increase
    the count by 1. If the number is not already located within cube_data,
    create a new entry for this sorted number with the (n**3) n-value and
    counts set to 0. They will be incrememted the following line.
    - Heavily influenced by nayuki's solution

    '''
    # n is the number of desired cubic permutations which are also cubes
    
    number_of_digits = 0 # A filter so that we only check for a 
    # solution every time the checked value gains a digit.
    
    cube_data = {} # Create dict to hold values and counts {int, counts}

    # Using itertools.count is generally faster than 'in range(...)'
    # Also, an end point need not be specified
    for i in itertools.count():
        cube = [int(x) for x in str(i**3)]
        cube.sort() # Sort so that all permutations can be compared easily
        check_val = ''.join(str(d) for d in cube)
        
        if len(check_val) > number_of_digits:
            solution = [smallest for (smallest, counts) in cube_data.values() 
                        if counts == n]
            if len(solution) > 0:
                return str(np.min(solution))
            cube_data = {} # Previous data can be erased
            number_of_digits = len(check_val)
        # i is the cube that the sorted number was made from. Init counts to 0
        smallest, counts = cube_data.get(check_val, (i, 0))
        cube_data[check_val] = (smallest, counts + 1)
        
                

#%%
import time
start = time.time()
min_cube = Cubic_Permutations(5)
end = time.time()
print(end - start)