# longest repeating character replacement in neetcode: find the longest substring with repeating character of k (that can be replaced) return its length
# Time complexity: O(m*n)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        charSet = set(s)

        for c in charSet:
            count = l = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1
                while (r-l+1)-count > k: # length of current window - count is more than k (invalid)
                    if s[l] == c:
                        count -= 1
                    l += 1
                res = max(res, r-l+1)
        return res
        
