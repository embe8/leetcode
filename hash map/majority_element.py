'''Problem: Majority Element
Given an array of nums, return the element that occurs more than floor n/2 or n//2 times
meaning meaning the largest integer less than or equal to n/2.

Example:

If n = 5, ⌊5/2⌋ = ⌊2.5⌋ = 2
If n = 4, ⌊4/2⌋ = ⌊2⌋ = 2
'''
# Time complexity: O(nlogn)
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mapList = {}
        for num in nums:
            if num in mapList:
                mapList[num] += 1
            else:
                mapList[num] = 1
        sortedList = sorted(mapList.items(), key=lambda x: x[1], reverse=True)
        return sortedList[0][0]
        
