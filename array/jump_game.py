'''Problem name: Jump Game
Given an array of integers, check if the end of the aray can be reached by 'jumping'
or moving towards the goal depending on current element value
For example: 
Approach: Start from end of array since if element before last element is 1 then 
last element can be reached (means can move 1 place to end of array) and the rest
of array doesn't need to be traversed
When index of current element and current element value is equal or more than goal,
shift the goal (last element) towards the front of the array
If first array element is reached (goal index == 0) then True, else False
'''

# Time complexity: O(n)
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        goal = len(nums)-1 # we only need to reach the final index
        # start from the end of array since if number before last
        # element is 1 then we can reach the goal without traversing
        # entire array
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        # since we shift goal by one til it reaches index 0 every
        # iteration, at the end we just check if we have reached
        # the first element
        return True if goal == 0 else False
          
        
