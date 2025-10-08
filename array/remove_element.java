// Problem: remove all elements equal to val in a given array and return the final array size
// Approach: Keep an index for the next element to keep/replace, 
// then if current element is not equal to val, keep the element and increment index

class Solution {
    public int removeElement(int[] nums, int val) {
        int k = 0; // Points to the next position to keep a value

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val) {
                nums[k] = nums[i]; // Keep this value
                k++;
            }
        }

        // After the loop, first 'k' elements in nums are the result
        return k;
    }
}

// What happens: ex. val = 2, arr = 1, 2, 3, 2:
// 1 not equal to 2 so keep it, 2 is equal to 2 so nothing happens until
// next iteration where nums[i] which is 3 will be compared with val
// and since k was not incremented what gets replaced is prev element 2
// so arr becomes 1 3 3 2
// next 3 is not replaced since last element 2 is equal to val
// return k which is the number of elements == val

