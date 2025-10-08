class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        // this is a java version of a submitted solution here originally in cpp
        // initialize variables to track indices in each array
        int i = 0;
        int j = 0;
        int k = 0;
        // array to store merged list
        int [] mergedList = new int[m+n];

        // while both nums1 and nums2 indices are less than size of each (m and n)
        while(i < m && j < n) {
            if(nums1[i] <= nums2[j])
            {mergedList[k] = nums1[i];
            i++;
            k++;
            }
       else{
        mergedList[k] = nums2[j];
        j++;
        k++;
       }}
        //handle leftover elements
        while(i<m){
            mergedList[k] = nums1[i];
            i++;
            k++;
        }
        while(j<n){
            mergedList[k] = nums2[j];
            j++;
            k++;
        }
        // should be in place
        for(int x=0;x<nums1.length;x++){
            nums1[x] = mergedList[x];
        }
    }
}
