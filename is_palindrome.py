# Time complexity: O(n)

class Solution(object):
    def isPalindrome(self, s):
        """
        Check if a string is a palindrome, ignoring non-alphanumeric characters and case.
        :type s: str
        :rtype: bool
        """
        # Initialize two pointers: one at the start, one at the end
        start = 0
        end = len(s) - 1
        
        # Move pointers toward each other until they meet
        while start < end:
            
            # Skip non-alphanumeric characters from the right
            # (spaces, punctuation, special chars)
            if not s[end].isalnum():
                end -= 1
                continue
            
            # Skip non-alphanumeric characters from the left
            # (spaces, punctuation, special chars)
            if not s[start].isalnum():
                start += 1
                continue
            
            # Compare characters (case-insensitive)
            # If they don't match, it's not a palindrome
            if s[start].lower() != s[end].lower():
                return False
            
            # Both characters match, move both pointers inward
            start += 1
            end -= 1
        
        # If we made it through the whole string without mismatches,
        # it's a palindrome
        return True

# with slice notation
# time complexity: O(n^2)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ''
        # create new string containing only alphanum chars
        for char in s:
            if char.isalnum(): # check if a letter or digit
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
            if char.isalnum(): # check if character or digit
                chars.append(char.lower())  # O(1) append
        
        cleaned = ''.join(chars)  # O(m) join (done once) avoids creation of new string every time with the code ' newString += char.lower() # convert to lowercase' in previous
        return cleaned == cleaned[::-1]
        
# another version with one less line of code
# no need to join can use the list and compare it with the reverse:
class Solution:
    def isPalindrome(self, s: string)->bool:
        # create a list to store the string to be checked
        word = []
        for char in s:
            if char.isalnum():
                word.append(char.lower())

        # compare the cleaned string to its reverse
        if word == word[::-1]:
            return True
        else:
            return False
