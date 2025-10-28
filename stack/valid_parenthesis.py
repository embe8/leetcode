'''Name: Valid Parenthesis (easy)
Given a string check if it's valid where valid means that every (,[,{ should be closed by its
corresponding closing bracket and in the correct order (for ex. ([]) is True, [(]) is False)
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        store = { ")": "(", "]":"[", "}" : "{"}
        for char in s:
            if char in store:
               # check if last element in stack is equal to the corresponding closing bracket for current element
                if stack and stack[-1] == store[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char) # store current element in stack if it's not present
        return True if not stack else False
            
        

            


