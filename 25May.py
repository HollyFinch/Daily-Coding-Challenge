#have to install numpy

import numpy as np

dictionary = {'no':'no', 'yes':'yes'}

crosswordMx = np.array([['n','p'], ['o', 'k']])
#shape returns size of the matrix, 2 by 2 in this case, so use either [0] or [1]
Mx_dimension = crosswordMx.shape[0]

for key, value in dictionary.items():
    print(f"Key: {key}")
    for letter in key:
        check_element = letter
        
        letter_position = np.argwhere(crosswordMx == check_element)

        if letter_position.size > 0:
            for position in letter_position:
                row,col = position
                print(f"Element '{check_element}' found at position: ({row}, {col})")
                
                if (row,col) == (0,0):
                    print(f"the letter '{check_element}' is in top left corner")
                
                if (row,col) == (Mx_dimension -1, Mx_dimension -1):
                    print(f"the letter '{check_element}' is in bottom right corner")
        
        else: print("not in my matrix")
        