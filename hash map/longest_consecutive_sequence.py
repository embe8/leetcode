'''Problem: Longest consecutive sequence
Given: a list of integers, return the length of the longest array of consecutive integers that can be formed
Example: [1,2,3,10,99,4] Output: 4 because 1,2,3,4 is the lcs
Approach: track the elements visited using a set and while the current element + 1 is in the set, increment streak
'''
# time complexity: O(n)
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0 # stores max streak length
        # store nums in set to remove duplicates
        setNums = set(nums)

        for num in setNums:
            # check if current element - 1 is already in set
            if num - 1 not in setNums:
                # means the current element is the first
                streak = 1 # current streak length
                # means num-1 is in setNums check if next expected is also
                while num + streak in setNums:
                    streak += 1
                # get longest streak so far
                count = max(count, streak)
        return count
                

# alternative solution with time complexity of O(nlogn)

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        count = 0
        nums.sort()
        i = 0
        expected, streak = nums[0], 0
        while i < len(nums):
            if nums[i] != expected:
                # set current element as the expected
                expected = nums[i]
                streak = 0
            while i < len(nums) and nums[i] == expected:
                i += 1
            streak += 1
            expected +=1
            # get max streak
            count = max(count, streak)
        return count
