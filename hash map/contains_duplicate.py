class Solution:
    def hasDuplicate(self, nums: List[int])->List[int]:
        mapList = {}
        for i in range(0, len(nums)):
            if nums[i] in mapList:
                if i != mapList[nums[i]]:
                    return True
            else:
                mapList[nums[i]] = i
        return False
