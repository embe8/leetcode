# brute force
'''
returns the index of the target int in a list if target is found
if not found, index of target is still returned
(its index if it was found in original list)
'''
def searchInsert(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    i = 0
    while (i < len(nums)):
        if nums[i] == target:
            return i
        i = i + 1
        # element not found:
    nums.append(target)
    nums = sorted(nums)
    return self.searchInsert(nums, target)

# optimal solution
def searchInsert(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    n = (len(nums) - 1) // 2
    l = len(nums)
    store = 0
    found = True
    if target not in nums:
        if target < nums[0]:
            return 0
        elif target > nums[-1]:
            return l
        for i in range(1, l):
            if nums[i - 1] <= target and nums[i] >= target:
                return i

    else:
        while found:
            print(n, store)
            if nums[n] == target:
                store += n
                return store
            elif nums[n] <= target:
                nums = nums[n + 1:]
                store += n + 1
                n = len(nums) // 2

            else:
                nums = nums[:n]
                n = (n) // 2





