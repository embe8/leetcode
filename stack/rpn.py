'''Problem name: Evaluate Reverse Polish Notation
Given: given an array of strings representing numbers and operators (+,-,*,/) that is a valid RPN expression,
return the final result of the entire evaluation, assuming division always truncates to zero
Approach: use a stack to store non operators, for addition and multiplication pop twice and do operation,
for subtraction and division, pop twice and subtract first popped from second popped element, same with division
'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for char in tokens:
            if char == '+':
                firstNum = stack.pop()
                secondNum = stack.pop()
                result = firstNum + secondNum
                stack.append(result)
            elif char == '-':
                # first elem popped is the last appended so it must be the subtrahend
                subtrahend, minuend = stack.pop(), stack.pop()
                stack.append(minuend - subtrahend)
            elif char == '*':
                # same logic as addition
                stack.append(stack.pop() * stack.pop())
            elif char == '/':
                # same logic as subtraction
                divisor, dividend = stack.pop(), stack.pop()
                stack.append(int(float(dividend) / divisor))
            else:
                stack.append(int(char))
        # return last element left which should be the result
        return stack[0]
        

            
        
