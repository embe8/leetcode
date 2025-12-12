# Neetcode
# Name: Valid Anagram
# Problem: given two strings s and t, return true if they are anagrams of each other
# approach: count number of elements in each string using a hash map and if hash maps are equal then they're anagrams
  # time complexity: O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # edge cases handling
        # if s or t is less than the other in length
        if len(s) != len(t): return False
        # use hash map to keep track of element = number
        mapS = {}
        mapT = {}
        for i in range(0, len(s)):
            if s[i] not in mapS:
                mapS[s[i]] = 1
            if t[i] not in mapT:
                mapT[t[i]] = 1
            # if it's in map increment value
            # get key (element count) and increment
            mapS[s[i]] = mapS.get(s[i], 0) + 1
            mapT[t[i]] = mapT.get(t[i], 0) + 1
        # check if both maps are equal
        if mapS == mapT: return True
        else: return False
