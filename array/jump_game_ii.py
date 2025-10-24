'''
Given an array of integers, find the minimum number of jumps
that you can take from index 0 to reach the end of the array
'''

# Greedy solution time complexity: O(n)
class Solution:
    def jump(self, nums: List[int]) -> int:
        # we need to count the jumps
        # keep track of the end of current jump
        jumps = 0
        current_end = 0
        farthest = 0
        for i in range(0, len(nums)-1): # no need to visit the last element
            farthest = max(farthest, nums[i] + i)

            if i == current_end:
                jumps += 1
                current_end = farthest
        return jumps
