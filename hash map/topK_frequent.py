class Solution:
    def topKFrequent(self, nums: List[int], k: int)->List[int]:
        mapList = {}
        for i, a in enumerate(nums):
            if a in mapList:
                mapList[a] += 1
            else:
                mapList[a] = 1
            
        sortedList = sorted(mapList.items(), key = lambda x:x[1], reverse = True)
        return [item[0] for item in sortedList [:k]]
