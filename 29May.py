import numpy as np

dictionary = {'no':'no', 'yes':'yes'}

crosswordMx = np.array([['n','p'], ['o', 's']])
Mx_dimension = crosswordMx.shape[0]

for key, value in dictionary.items():
    print(f"Key: {key}")
    key_len = len(key)

    for i, letter in enumerate(key):
        check_element = letter
        
        letter_position = np.argwhere(crosswordMx == check_element)

        if letter_position.size > 0:
            for position in letter_position:
                row, col = position
                print(f"Element '{check_element}' found at position: ({row}, {col})")
                
                if (row, col) == (0, 0):
                    print(f"The letter '{check_element}' is in the top left corner")
                
                if i + 1 < key_len:
                    next_letter = key[i + 1]
                    next_letter_position = np.argwhere(crosswordMx == next_letter)
                    
                    if next_letter_position.size > 0:
                        first_occurrence_of_letter = next_letter_position[0]
                        second_letter_row = first_occurrence_of_letter[0]
                        second_letter_col = first_occurrence_of_letter[1]

                        if second_letter_row == row + 1 and second_letter_col == col:
                            print("move down")
                        elif second_letter_row == row and second_letter_col == col + 1:
                            print("move right")
                    else:
                        print(f"Next element '{next_letter}' not found in the crossword matrix.")
        else:
            print(f"Element '{check_element}' not found in the crossword matrix.")
