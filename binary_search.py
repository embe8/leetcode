'''Problem: Binary Search
Given an array of numbers arranged in ascending order and a target number, return the index
of the element that is equal to the target
Approach: use two pointers and keep track of the middle element, adjusting the pointers based
on if the middle element is less than or greater than the target number
'''
# Time complexity: O(logn) versus O(n) time complexity of for loop sorting without use of binary search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            # left + right can result in overflow
            # get middle element, right - 1 since 0 index
            middle = left + ((right-left) // 2)
            if nums[middle] > target: # if element is more than target, means its on the left side (less) so minus one
                right = middle - 1
            elif nums[middle] < target: # if element is less than target, means its on the right side (more) so plus one
                left = middle + 1
            else:
                return middle
        return -1

# Same code but more comments/explanation
class Solution:
    def search(self, nums: List[int], target: int)->int:
        # initialize left and right pointers
        left, right = 0, len(nums) - 1

        while left <= right:
            # initialize middle(should be left + right but may overflow)
            middle = left + ((right-left)//2)
            if target > nums[middle]: # means all elements to the left of middle
            # is less than target so move left ptr to the right
                left = middle + 1
            elif target < nums[middle]:
                right = middle - 1
            else: return middle
        return -1
