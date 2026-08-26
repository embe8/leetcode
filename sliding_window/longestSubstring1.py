# for lonest string without repeating characters: given a string, find the longest occurring consecutive substring
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res

# Time complexity: O(n) both
class Solution:
    def lengthofLongestSubstring(self, s: str) -> int:
        mp = {}
        left = 0
        res = 0
        for r in range(len(s)):
            if s[r] in mp:
                left = max(mp[s[r]] + 1, left) # left is incremented if s[r] is mp
            mp[s[r]] = r # store index for current element , mp will contain element = index
            res = max(res, r - left + 1) # compare current sliding window with previous result
        return res
        
