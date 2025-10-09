// Name: Rotate Array
// Problem: Given an array and value k, rotate the array to the right k times

class Solution {
    public void rotate(int[] nums, int k) {
        k = k % nums.length;  // Normalize k

        if (k != 0) {
            int n = nums.length;
            // copy last k elements
            int[] copyOfEnd = Arrays.copyOfRange(nums, nums.length-k, nums.length); 
            // copy first element index 0 to k
            int[] copyOfStart = Arrays.copyOfRange(nums, 0, nums.length-k);
            // merge arrays from 0 to k for first array and k to length of array - k
            System.arraycopy(copyOfEnd, 0, nums, 0, k);
            System.arraycopy(copyOfStart, 0, nums, k, n-k);
    }
    }
}
