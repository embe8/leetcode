# Name: Rotate Array
# Problem: Given an array and k, rotate the array to k places to the right
# Use array slicing, replace first k elements with last k elements and the rest with the remaining elements (not sliced)

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
      # handle edge case if array is 0 or k is 0
      if nums == 0 or k == 0: return nums
      else:
      # else check if k is more than the length of array
        k %= len(nums)
      # swap sliced first k elements with last k elements and handle the remaining
      nums[:k], nums[k:] = nums[:-k], nums[-k:]

# Example: Given k = 10 nums = 1,2,3,4,5,6,7
# k is more than length of array so 10%len(nums)=3, new k = 3
# first k elements will become [:-k] which are the last k elements (5,6,7)
# Remaining elements 1,2,3,4 will be placed after so 5,6,7,1,2,3,4 is the final array
