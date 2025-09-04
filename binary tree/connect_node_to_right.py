'''
Given the root of a binary tree (general), set all next pointers to their right nodes
'''
from collections import deque

class Solution(object):
    def connect(self, root):
        if not root:
            return None

        # Initialize queue with root node
        queue = deque([root])
        # Process each level
        while queue:
            size = len(queue)
            prev = None

            for i in range(size):
              # Process each node in each level
                node = queue.popleft()
                
                if prev:
                    prev.next = node
                prev = node
              # Place left and right children of current node so they are processed
              # In the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Last node in the level should point to None
            prev.next = None
        # Return the modified binary tree with next pointers set to right node
        return root
