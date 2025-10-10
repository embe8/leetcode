# Name: Two Sum
# Problem: Given a target value and a list of integers, find the indices of the elements that add up to target

# Optimized solution: O(n)
# Approach: Use hash map to map index to element, find the difference between element and target and check if its in the list

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}  # Storage to map number to its index
        for i, num in enumerate(nums):
            complement = target - num  # Find the difference between target number and current element
            if complement in num_map:  # Check if the difference exists in the given list
                return [num_map[complement], i]  # Return the index of the difference in hash map and the index of the current element
            num_map[num] = i  # Otherwise, create a look up table with element as the key and value as its index

# Brute force with O(n^2) time complexity

