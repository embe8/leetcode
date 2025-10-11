# Name: Contains Duplicate II
# Problem: Given a list of integers and target value k, check if i and j exists in list such that list[i] == list[j]
# and abs(i-j) <= target value k
# Approach: use an unsorted map/hash map to keep track of elements, if current element not in map, insert it
# If element is in map, get its index and compare current element index - same element index checking if difference
# is less than or equal to target value k

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map_list = {}  # initialize map
        for i in range(0, len(nums)):
            if nums[i] in map_list:
                sameIndex = map_list[nums[i]]  # if current element is in map, get its index
                if abs(i - sameIndex) <= k:  # check the difference of current element index i and same element index j
                    return True  # if difference less than or equal than target k
            map_list[nums[i]] = i  # if current element not in map, insert it
        return False  # difference is not <= k or no same elements
        
