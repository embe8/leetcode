// Problem: Given a sorted list of integers in ascending order, return the number of unique elements k and the array with the first k elements being the unique element
// Approach: Start with index n = 1 instead of 0, compare it with preceding element, in case of unique elements, move it forward in the array

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        // handle empty or array with size 1
        if (nums.size() <= 1)
        {
            return nums.size();
        }
        // else traverse vector
        int k = 1;
        for(int i = 1;i< nums.size();i++)
        {
            //check if not equal with previous element
            if(nums[i] != nums[i-1])
            {
                nums[k] = nums[i];
                //increment k since unique element
                ++k;
            }
        }
        return k;
    }
};
