'''Problem name: Trapping Rain Water (Leetcode)
Given an array of integers representing the height of a bar, return the max
amount of water that can be trapped between the bars
Approach: Use two pointers, left and right, keep track of the max on left and right
move pointer according to which is less, subtract the current height from the max
to get amount of water it can hold
'''
# Time complexity: O(n) using two pointer approach
class Solution:
    def trap(self, height: List[int]) -> int:

        if not height: return 0
        # initialize pointers
        left, right = 0, len(height)-1
        # store sum of heights
        result = 0
        # initialize max values on left and right
        maxLeft, maxRight = height[left], height[right]

        while left < right:
            if maxLeft < maxRight:
                left += 1
                maxLeft = max(maxLeft, height[left])
                result += maxLeft - height[left]
            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                result += maxRight - height[right]

        return result




        
        
