// C++ version of solution to Contains Duplicate II (python)

#include <unordered_map>

class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
            unordered_map<int, int> mapIndex;
            // traverse through vector
            for(int i=0;i<nums.size();i++){
                if(mapIndex.find(nums[i]) != mapIndex.end()) // not equal to means nums[i] was found
                {
                    int sameIndex = mapIndex[nums[i]]; // get the index (value) by using its key (nums[i])
                    if(i - sameIndex <= k){
                        return true;
                    }
                }
                mapIndex[nums[i]] = i; // if current element not in list
            }    
            return false;
    }
};
