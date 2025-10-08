# Python version of remove_element.java
# Uses the same approach, only checks if array element not equal to val
# If so, it keeps it and increments k which keeps track of elements replaced

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0 # keep track of element to replace or keep
        # traverse thru list
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
            
        return k
