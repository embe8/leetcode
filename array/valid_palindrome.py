# Problem: Given a string (can have spaces/non alphanumeric characters), check if it's a palindrome
# Approach: Create new string, adding only alphanumeric characters to it, reverse it, and compare the two
# Time complexity: O(n)

class Solution:
    def isPalindrome(self, s: str) -> bool:
      newString = ''
      for char in s:
        if char.isalnum():
          newString += char.lower()
      # compare new string with its reverse
      return newString == newString[::-1]

# Alternate solution using list to store new word
# Time complexity: O(n)
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

            
