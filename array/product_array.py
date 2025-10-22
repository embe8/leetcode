'''Problem name: Product of array except self
Given an array of integers, return an array that contains the product of all elements
except for the current element
For example: array = [1,2,3,4]
output: array = [24, 12, 8, 6]
Approach: two for loops where first loop computes the product of all elements to the left
of current element and second for loop computes the product of first loop and all elements
to the right of current element
'''

# time complexity: O(n)
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # first initialize left product
        # and container of final result
        left_product = 1
        array_size = len(nums)
        result = [0] * array_size

        # first get the product of all elements to the left
        # of current element
        for i in range(0, array_size):
            # before current index, store product
            result[i] = left_product
            # multiply current product by current element
            left_product *= nums[i]

        right_product = 1
        # backwards multiplication starting from end of array
        # parameters of loop (start, stop, step)
        for i in range(array_size-1, -1, -1):
            # multiply left product by right product
            result[i] *= right_product
            # multiply right product by current element
            right_product *= nums[i]
        return result

        

        
