#have to install numpy

import numpy as np

dictionary = {'no':'no', 'yes':'yes'}

crosswordMx = np.array([['n','p'], ['o', 'k']])

for key, value in dictionary.items():
    print(f"Key: {key}")
    for letter in key:
        check_element = letter
        
        letter_position = np.argwhere(crosswordMx == check_element)

        if letter_position.size > 0:
            for position in letter_position:
                row,col = position
                print(f"Element '{check_element}' found at position: ({row}, {col})")
        
        else: print("not in my matrix")
        