'''Problem name: Search 2D Array
Given a target integer and a 2D array of integers, return True if the
2D array contains the target, else return False
Approach: Use binary search twice, once through the rows/columns and 
then another for scanning through the row
Time complexity: O(log(m) + Olog(n)) 
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows_length, columns_length = len(matrix), len(matrix[0])

        # we scan all rows first and do binary search on each
        top, bottom = 0, rows_length - 1
        while top <= bottom:
            row = (top + bottom) // 2
            # if target is less than the last element on the row
            if target > matrix[row][-1]:
                # this means the element can be found in the later rows
                # so we move the top row pointer forward
                top = row + 1
                # else if target is greater than the first element in the row
                # this means the target can be found in the rows before the current one
                # so we move the bottom row one row up to scan elements with lower values
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break # 
        if not (top <= bottom): return False
        # binary search on the current row
        row = (top + bottom) // 2
        left, right = 0, columns_length - 1
        while left <= right:
            middle = (left + right) // 2
            # if target is more than current element
            # move left ptr forward (since array is sorted in ascending order)
            if target > matrix[row][middle]:
                left = middle + 1
            # if target is less than current element, move
            # right ptr backwards to scan lesser elements 
            elif target < matrix[row][middle]:
                right = middle - 1
            else:
                return True
        return False
