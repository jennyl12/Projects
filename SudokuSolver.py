from pprint import pprint

def find_next_empty(puzzle):
    # finds the next row, col on the puzze that is empty --> rep with -1
    # return row, col tuple (or (none, None) if there is none)

    # keep in mind that we are using 0-8 for our indices
    for r in range(9):
        for c in range(9): # rage(9) is 0, 1, 2 ... 8
            if puzzle[r][c] == -1:
                return r, c

    return None, None # if no spaces in the puzzle are empty (-1)

def is_valid(puzzle, guess, row, col):
    #figures out whether the guess at the row/col of the puzzle is a vlid guess
    #returns True if is valid, False if not

    #start with the row
    row_values = puzzle[row]
    if guess in row_values:
        return False

    #column next
   # col_values = []
    #for i in range(9):
       # col_values.append(puzzle[i][col])
    col_values = [puzzle[i][col] for i in range (9)]
    if guess in col_values:
        return False
    
    # and then the square
    # now we want to see where the 3x3 square starts
    #and iterate over the 3 values in the row/column
    row_start = (row // 3) * 3 #1//3 = 0, 5//3 = 1,...
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    
    return True

def solve_sudoku(puzzle):
    #solve sudoku using a backtracking technique
    #puzzle is a list of lists where each inner list is a row in the sudoku puzle
    #program returns whether a solution exists and if not, prints out "solution does not exist"
    # mutates pizzle to be the solution (if soltion exists)

    #step 1: see where on the puzzle you can go
    row, col = find_next_empty(puzzle)

    # step 1.1
    if row is None:
        return True
        
    #step 2: if there is a place to put a number, then make a guess between 1 and 9
    for guess in range (1,10): #range(1,10) is 1, 2, 3, ... 9
        #step 3: check if this is a valid guess
        if is_valid(puzzle, guess, row, col):
            #step 3.1: if this valid is true, then place that guess on the puzzle
            puzzle[row][col] = guess
            # now recurse using this puzzle
            #step 4: recursively call our function
            if solve_sudoku(puzzle):
                return True
        
        #step 5: if not valid OR if our guess does not solve the puzzle, then we need to
        #backtrack and try a new number
        puzzle[row][col] = -1 #reset the guess

    #step 6: if none of the numbers that we try work, then this puzzle is UNSOLVEABLE
    return False

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    pprint(example_board)