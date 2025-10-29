'''Problem: Minimum Stack
Create a class MinStack with functions to initialize class, pop, push
top, and return the min value from the stack. All functions should 
have O(1) time complexity
Approach: Use two stacks, one to keep track of the min value
'''

class MinStack:

    def __init__(self):
        self.min = float('inf')
        # initialize stack
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        # take min of current value and top of min stack, if empty just take current val
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
            

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        # we're appending the min on top in push() so just return the top element
        return self.minStack[-1]
        
