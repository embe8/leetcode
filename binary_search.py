'''Problem: Binary Search
Given an array of numbers arranged in ascending order and a target number, return the index
of the element that is equal to the target
Approach: use two pointers and keep track of the middle element, adjusting the pointers based
on if the middle element is less than or greater than the target number
'''
# Time complexity: O(logn)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            # left + right can result in overflow
            # get middle element, right - 1 since 0 index
            middle = left + ((right-left) // 2)
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle
        return -1
        
