# Neetcode problem name: Group Anagrams
# Problem: Given a list of strings, return the list where elements that are anagrams of each other are grouped together
# For example: Input: strs = ["act","pots","tops","cat","stop","hat"]
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

# Approach: Use a dictionary to store a unique key and value (list of strings)
# Key used: should be unique so in this case, a list of characters (alphabet: a-z) was chosen and their count
# if word has same key as what's in the map, it is added to the values associated with the key
# as a result, a list of strings that have the same key (thus, they are anagrams of each other since same element count) are returned
# Note: defaultdict automatically inserts elements that are not yet inserted

# time complexity: O(n*m)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # keep track of number of elements in each string
        mapList = defaultdict(list)
        # traverse list of strings
        for i in range(0, len(strs)):
            # create a unique key for the string (list of characters/alphabet in this case)
            # initialize key container which is a list of 26 elements
            count = [0] * 26
            for char in strs[i]:
                count[ord(char)-ord('a')] += 1 # inside [] is index where ord(char) gets ascii
                # ex. ord('b) = 98 minus ord('a') = 97 = 1 so its index is 1 and a has index 0
                # plus 1 increments the value or count of the element/char
                # convert list to tuple to make it immutable/hashable (list is not, it'smutable)
            key = tuple(count)
                # add the word to the values associated with the key
            mapList[key].append(strs[i])

        return list(mapList.values())
        
