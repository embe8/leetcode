'''
Problem: Given the root of the binary tree, find its maximum depth
'''


# Recursive solution: O(n)
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        if not root:
            return 0
        left = self.maxDepth(root.left) # Traverse left subtree recursively
        right = self.maxDepth(root.right) # Traverse right subtree recursively

        return 1 + max(left, right) # Return the greater of left and right subtree heights

# other recursive version
class Solution(objec):
    def maxDepth(self, root):
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Iterative solution: O(n)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # check if empty
        if not root: return 0
        # store root in queue
        queue = deque([root])
        depth = 0
        # traverse tree
        while queue:
            # get number of nodes in current level
            level_size = len(queue)

            for __ in range(level_size):
            # get node at front of queue, root is the first
                current = queue.popleft()

                # store next nodes to visit
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            # after processing one level increase depth
            depth += 1
            

        return depth

# BFS alternate version:
# time complexity: O(n)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        if not root: return 0
        else: q.append(root)

        level = 0

        while q:
            for i in range(len(q)):
                # visit each level
                node = q.popleft()
                if node.left:
                    q.append(node.left) # visit next
                if node.right:
                    q.append(node.right)
            level += 1
        return level

# DFS version
# time complexity: O(n)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        s = [[root, 1]]

        maxDepth = 0

        while s:
            node, depth = s.pop()
            if node:
                maxDepth = max(maxDepth, depth)
                s.append([node.left, depth + 1]) # visit next
                s.append([node.right, depth + 1])
        return maxDepth


        


