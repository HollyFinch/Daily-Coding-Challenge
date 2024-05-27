#have to install numpy

import numpy as np

dictionary = {'no':'no', 'yes':'yes'}

crosswordMx = (['n','p'], ['o', 'k'])

# for each letter I am going to find where its position is
check_element = 'k'

# Check if the element is in the top-left position
in_Top_Left = crosswordMx[0][0] == check_element

print(f"Element '{check_element}' in top-left:", in_Top_Left)

in_Top_Row = check_element in crosswordMx[0]

print(f"Element '{check_element}' in top row:", in_Top_Row)

in_Bottom_Row = check_element in crosswordMx[1]

print(f"Element '{check_element}' in bottom row:", in_Bottom_Row)