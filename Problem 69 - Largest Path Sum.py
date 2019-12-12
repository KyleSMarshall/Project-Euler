'''
Largest sum pathfinding
'''

import numpy as np
import pandas as pd

triangle = [[np.nan for x in range(0,100)] for m in range(0,100)]
tri_input = pd.read_csv('p067_triangle.txt', header=None)

for i in range(0,100):
    values = [x for x in tri_input.iloc[i]]
    values = [int(x) for x in values[0].split()]
    for value in range(0,len(values)):
        triangle[i][value] = values[value]
        
#%%
'''
The loop below is a simple pathfinding algorithm which simply checks one row
ahead and assigns the maximum valued node in that row to be the new node value.

Improvements can be made to: 
- Discourage edge-hugging which this algorithm may be prone to due to 
  asymmetric triange column growth.
- Search the possible paths for multiple rows ahead.
  Searching n rows ahead increases the number of potential_paths by 3^n
'''
node=0
path_sum=0
for depth in range(0,99):
    path_sum = path_sum + triangle[depth][node]
    potential_paths = []
    if node!=0:
        potential_paths.append(triangle[depth+1][node])
        potential_paths.append(triangle[depth+1][node+1])
        potential_paths.append(triangle[depth+1][node-1])
    else:
        potential_paths.append(triangle[depth+1][node])
        potential_paths.append(triangle[depth+1][node+1])
        
    max_path = np.max(potential_paths)
    max_path_ind = potential_paths.index(np.max(potential_paths))
    node = max_path_ind
        
