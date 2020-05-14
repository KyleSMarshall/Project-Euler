import pandas as pd
import numpy as np
from collections import deque
import time

class Path_Sum():
    
    
    def loader(self, name):
        '''
        Loads the data matrix and prepares it for the [min_path] algorithm.
        
        Keyword arguments:
        name -- String: full name (inc. extension) of the matrix file
        Returns:
        data -- Numpy array: prepared matrix
        '''
        data = np.array(pd.read_csv(name, header=None))
        
        # Add a box of infities around the data matrix
        
        # Rows of infs
        row = np.shape(data)[1]
        inf = [float('inf') for x in range(row)]
        # Vertically stack above and below the matrix
        data = np.vstack((inf, data, inf))
        
        # Columns of infs
        col = np.shape(data)[0]
        inf = [[float('inf')] for x in range(col)]
        # Horizontally stack left and right of the matrix
        data = np.hstack((inf, data, inf))
        
        return data
    
    
    def min_path(self):
        '''
        Computes the minimum path sum from the top-left corner of the matrix to the bottom-right.
        Utilizes a BFS algortithm to iteratively update the matrix values to the min_path as the possible paths are traversed.
        Breaks the problem down into a series of min_path problems and building the solutions up to the final 80x80.
        
        Returns:
        data[80][80] -- Float: Value of the minimum path sum.
        '''
        data = self.loader('p081_matrix.txt')
        
        # Use a BFS approach
        queue = deque([(1,2), (2,1)])
        visited = set()
        while queue:
            # Obtain row, col indices
            [row, col] = queue.popleft()
            # Modify the current matrix cell to be itself plus the minimum of the cells directly above and to the left
            data[row][col] = data[row][col] + min(data[row-1][col], data[row][col-1])
            
            # Conditions to append new indices to the queue
            if row+1 < len(data)-1 and (row+1, col) not in visited:
                queue.append((row+1, col))
                visited.add((row+1, col))
            
            if col+1 < len(data[0])-1 and (row, col+1) not in visited:
                queue.append((row, col+1))
                visited.add((row, col+1))
                
        return data[80][80]
                
                
'Answer is =  427337 || Time ellapsed =  33.80 ms'



'''
Another approach which doesn't require the initial data augmentation would be to implement my process above
using a series of for-loops.

Entire code:
'''
class Solution:

    def min_path(self):
        data = np.array(pd.read_csv('p081_matrix.txt', header=None))

        for i in range(1, data.shape[1]):
            data[0][i] += data[0][i-1]

        for i in range(1, data.shape[0]):
            data[i][0] += data[i-1][0]

        for i in range(1, data.shape[1]):
            for j in range(1, data.shape[0]):
                data[j][i] += min(data[j-1][i], data[j][i-1])

        return data[-1][-1]
        
'Answer is =  427337 || Time ellapsed =  27.11 ms'



'''
This can also be done using dynamic programming and recursive function calls.
'''
import pandas as pd
import numpy as np

class Solution:
    
    def __init__(self):
        # Keep a dict showing the minimum path from an index onward
        self.min_path = {}
        
    def minPathSum(self):
        grid = np.array(pd.read_csv('p081_matrix.txt', header=None))
        
        m = len(grid)
        n = len(grid[0])
        
        self.helper(grid, (0,0), m, n)
        return self.min_path[(0,0)]
        
        
    def helper(self, grid, ind, rows, cols):
        # Check in ind are already in the cache
        if ind in self.min_path:
            return self.min_path[ind]

        if ind == (rows-1, cols-1):
            self.min_path[ind] = grid[ind[0]][ind[1]]
            return self.min_path[ind]

        if ind[0] == rows-1:
            self.min_path[ind] = grid[ind[0]][ind[1]] + self.helper(grid, (ind[0], ind[1] + 1), rows=rows, cols=cols)
            return self.min_path[ind]
        if ind[1] == cols-1:
            self.min_path[ind] = grid[ind[0]][ind[1]] + self.helper(grid, (ind[0] + 1, ind[1]), rows=rows, cols=cols)
            return self.min_path[ind]
        self.min_path[ind] = grid[ind[0]][ind[1]] + min(self.helper(grid, (ind[0] + 1, ind[1]), rows=rows, cols=cols), self.helper(grid, (ind[0], ind[1] + 1), rows=rows, cols=cols))

        return self.min_path[ind]
        
'Answer is =  427337 || Time ellapsed =  12.10 ms'
