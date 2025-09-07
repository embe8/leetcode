# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        result = []
        queue = deque([(root, 0)])  # node and level

        while queue:
            node, level = queue.popleft()

            # Add a new list if we're entering a new level
            if len(result) <= level:
                result.append([])

            # Normal order for even levels, reversed order for odd levels
            if level % 2 == 0:
                result[level].append(node.val)
            else:
                result[level].insert(0, node.val)  # insert at front for zigzag

            # Always enqueue children in normal left-right order
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return result
