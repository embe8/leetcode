# Time complexity: O(n)

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start = 0
        end = len(s) - 1
        while start < end:
            if not s[end].isalnum():
                end -= 1
                continue
              
            if not s[start].isalnum():
                start += 1
                continue

            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True

# with slice notation
# time complexity: O(n^2)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ''
        # create new string containing only alphanum chars
        for char in s:
            if char.isalnum():
                newString += char.lower() # convert to lowercase
        # compare new string with its reversed version
        return newString == newString[::-1]
'''Notes:
This is string slicing that reverses the string.
Slicing syntax: string[start:end:step]

[::-1] means: start at the end, go to the beginning, step backwards by 1'''

# improved version of above
# time complexity: O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []  # Use list instead
        for char in s:
            if char.isalnum():
                chars.append(char.lower())  # O(1) append
        
        cleaned = ''.join(chars)  # O(m) join (done once) avoids creation of new string every time with the code ' newString += char.lower() # convert to lowercase' in previous
        return cleaned == cleaned[::-1]
