// Problem name: Remove duplicates from sorted array II
// Problem desc: Given a sorted array in ascending order where at most an element can appear twice, 
// return the array with the first k unique elements 
// Approach: Same with sorted array I but with k = 2 since an element is allowed to appear twice

class Solution {
    public int removeDuplicates(int[] nums) {
        // handle array with less than 2 elements
        if(nums.length <= 2){
            return nums.length;
        }
        // else traverse array
        int k = 2;
        for(int i=2;i<nums.length;i++)
        {
            if(nums[i] != nums[k-2])
            {
                nums[k] = nums[i];
                ++k;
            }
        }
        return k;
    }
}
