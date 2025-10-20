'''Problem name: Valid sudoku
Problem: Given board of NxN elements where N=9, check if its a valid sudoku meaning
each row should contain 1-9 digits without duplicates, same for each column and each 3x3 submatrix,
and return True if valid else False
Approach: use 2d arrays of False values to track if a cell is visited, get normalized index
so that 1-9 index becomes 0-8 to track cell number in matrix'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # initialize 2d arrays to track if visited
        row_visited = [[False] * 9 for _ in range(9)]
        col_visited = [[False] * 9 for _ in range(9)]
        box_visited = [[False] * 9 for _ in range(9)]

        # iterate through the each cell in 9x9 board/matrix
        for row_index in range(9):
            for col_index in range(9):
                cell_value = board[row_index][col_index]

                if cell_value == '.': # check if empty and skip if so
                    continue
                # make 1-9 index 0-8
                normalized_index = int(cell_value) - 1
                # compute where in the 3x3 submatrix the cell is
                box_index = (row_index // 3) * 3 + (col_index // 3) # submatrix index
                # check if value already exists in current row, column or submatrix
                if (row_visited[row_index][normalized_index] or col_visited[col_index][normalized_index] or box_visited[box_index][normalized_index]):
                    return False
                # mark place as visisted in current row, column or submatrix 
                row_visited[row_index][normalized_index] = True
                col_visited[col_index][normalized_index] = True
                box_visited[box_index][normalized_index] = True
        # no duplicates found
        return True


            



        
