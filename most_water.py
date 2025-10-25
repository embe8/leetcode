'''
Given an array of integers with its elements being the height of a container,
return the max area that can be covered by water
Approach: use two pointers to keep track of the width (right pointer - left pointer) 
where right_pointer is the length of the list and left is 0, get the width using the x-axis
and multiply this with the min height, and keep track of the max area
'''

# Time complexity: O(n)
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_pointer, right_pointer = 0, len(heights)-1
        max_area = 0

        while left_pointer < right_pointer:
            # x-axis is the width
            width = right_pointer - left_pointer
            height = min(heights[left_pointer], heights[right_pointer])
            area = width * height
            max_area = max(area, max_area)
            
            # moving the left pointer to the right might increase max_area
            if heights[left_pointer] < heights[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

        return max_area

        

        
