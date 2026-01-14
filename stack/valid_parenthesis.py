'''Name: Valid Parenthesis (easy)
Given a string check if it's valid where valid means that every (,[,{ should be closed by its
corresponding closing bracket and in the correct order (for ex. ([]) is True, [(]) is False)
'''

'''
The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''

'''Example input:
Input: s = "([{}])"

Output: true
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        store = { ")": "(", "]":"[", "}" : "{"}
        for char in s: # only checks the keys (closing brackets) so first iteration reverts to else: stack.append(char)
            if char in store:
               # check if last element in stack is equal to the corresponding closing bracket for current element
                if stack and stack[-1] == store[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char) # store current element in stack if it's not present
        return True if not stack else False
            
        

            


