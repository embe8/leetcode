'''Problem: ThreeSum
Given an array of integers, return three elements as a list such that they sum to 0
and their indices are not equal. Do not include duplicates of the triplets.
Approach: Use two pointers, left starts at 0, right at the end, check if sum of
current element and the elements at the pointers equal to 0, else move pointers
accordingly
'''

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i, a in enumerate(nums):
            # if current element and previous element and current not the first element
            # means they're duplicates, skip
            if i>0 and a==nums[i-1]:
                continue
            left, right = i+1, len(nums)-1 # first element cant be second element
            while left < right:
                threeSum = a + nums[left] + nums[right]
                # if sum is greater than 0, decrease right since smaller elements are to the left
                if threeSum > 0:
                    right -= 1
                # if sum is less than 0, increase left since greater elements are to the right
                elif threeSum < 0:
                    left += 1
                # else threeSum is equal to 0 so add to result list
                else: 
                    result.append([a, nums[left], nums[right]])
                    left += 1
                    # avoid duplicates at left pointer (right pointer corrects itself using prev if statement)
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        return result
                    
            
