'''Problem name: Set Matrix to Zeroes
Problem: Given nxn matrix, if a row or column contains 0, the corresponding row and column of the cell that is 0 should all be converted to zeroes
Approach: Use two arrays to keep track of rows and columns with zeroes, traverse matrix twice--first to mark rows/columns with zeroes and
Second to set marked rows and columns to have all elements be zeroes
'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # initialize two arrays
        sizeRow = len(matrix)
        sizeCol = len(matrix[0])

        row_to_zeroes = [False] * len(matrix)
        col_to_zeroes = [False] * len(matrix[0])

        # traverse to check if any rows/cols contain zero
        for row_index in range(0, sizeRow):
            for col_index in range(0, sizeCol):
                if matrix[row_index][col_index] == 0:
                    row_to_zeroes[row_index] = True
                    col_to_zeroes[col_index] = True

        # second pass to convert marked rows/cols to have elements all equal to 0
        for row_index in range(0, sizeRow):
            for col_index in range(0, sizeCol):
                if row_to_zeroes[row_index] or col_to_zeroes[col_index] == True:
                    matrix[row_index][col_index] = 0
