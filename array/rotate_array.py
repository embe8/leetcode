# Python version of the Java solution for Rotate array
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # for loop through array
        # index + 3

        #if index + k is more than size of array - 1
        # k - (size of array - index ) 
        if len(nums) == 1 or k == 0:
            nums = nums
        #swap 
        else:
            k %= len(nums)
            if k == 0:
                return nums
            else:
              # last k elements [-k:] becomes first k elements [:k]
              # the remaining elements are appended
                nums[:k], nums[k:] = nums[-k:], nums[:-k]

# Alternative solution: more concise

class Solution(object):
    def rotate(self, nums, k):
      n = len(nums)
      k = k%n
      nums[:] = nums[n-k:] + nums[:n-k]
                
