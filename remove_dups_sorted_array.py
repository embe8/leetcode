# Problem name: Remove Duplicates from Sorted Array
# Given a sorted array of integers return the number of unique elements

class Solution(objec):
    def removeDuplicates(self, nums):
        if len(nums) <= 1:
            return 1

        k = 1

        for i in range(1, len(nums)):
            if(nums[i] != nums[i-1]):
                nums[k] = nums[i]

                k += 1
        return k
            
