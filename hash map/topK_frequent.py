# Given an array of integers, return the top K elements in any order

class Solution:
    def topKFrequent(self, nums: List[int], k: int)->List[int]:
        mapList = {}
        for i, a in enumerate(nums):
            if a in mapList:
                mapList[a] += 1
            else:
                mapList[a] = 1
            
        sortedList = sorted(mapList.items(), key = lambda x:x[1], reverse = True) # take the items (ints) and sort them in descending order, use the frequency as the basis for sorting
        return [item[0] for item in sortedList [:k]] # only take the first element (the int) of every tuple from the sortedList 
