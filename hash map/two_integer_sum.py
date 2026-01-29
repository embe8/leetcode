'''Problem name: Two Integer Sum II (neetcode) or Two Sum II - Input Array is Sorted (leetcode)
Problem: Given a sorted array (ascending order) and a target integer, return the indices of two elements as a list such that
both elements sum to target
Approach: use a hash map to keep track of the  index of each element where value is the index and key is the element
Check for target-current element in the for loop and get the index for the difference
'''
# Time complexity: O(n)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        maplist = {}
        for i in range(len(numbers)):
            if target - numbers[i] in maplist:
                minuend = target - numbers[i]
                index = maplist[minuend]
                if i < index or index < i:
                    return sorted([i+1, index+1])
            maplist[numbers[i]] = i
        
# same space complexity of O(n) but uses get function of map
class Solution:
    def twoSum(self, numbers: List[int], target: int)->List[int]:
        mapList = {}
        for i in range(len(numbers)):
            # get the value we're looking for
            difference = target - numbers[i]
            # get its index
            if difference in mapList:
                index = mapList.get(difference, 0)
                if index != i:
                    return sorted([index+1, i+1])
            mapList[numbers[i]] = i
#  Binary Search solution with time complexity: O(nlogn) space complexity: O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int)->List[int]:
        for i in range(len(numbers)):
            left, right = i + 1, len(numbers)-1
            diff = target - numbers[i]
            while left <= right:
                mid = left + (right-left)//2
                if numbers[mid] == diff:
                    return [i + 1, mid + 1]
                elif numbers[mid] < diff:
                    left = mid + 1
                else: right = mid - 1
        return []
            
