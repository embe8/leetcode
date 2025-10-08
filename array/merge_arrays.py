# Problem: Given two sorted lists of ascending order, merge them into one list in ascending order as well
# Do not place merged list in new list--use original list1

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # this solution is the python version of a previous submission here in cpp
        # initialize variables to track indices in each list
        merged_list = []
        i = 0
        j = 0
        # while both nums1 and nums2 contain elements
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                merged_list.append(nums1[i])
                # increment nums1 index
                i += 1
            else:
                merged_list.append(nums2[j])
                j += 1
        # check for left over elements
        while i < m:
            merged_list.append(nums1[i])
            i += 1
        while j < n:
            merged_list.append(nums2[j])
            j += 1
        for i in range(len(merged_list)):
            nums1[i] = merged_list[i]




        
