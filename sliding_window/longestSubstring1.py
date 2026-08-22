# for non repeating
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
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, 1)
            m[s[r]] = r
            res = max(mp[s[r]] - 1, r - l + 1)
        return res
        
