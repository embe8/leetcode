'''
Problem: Given a binary tree, traverse it in zigzag order (root, from right to left, vice versa)
Solution: Same as level order traversal except we need to reverse order of nodes for odd levels
'''

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

# Alternate solution, uses same logic but saves memory by not storing level number

from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root: return []
        tree_queue = deque([root])
        result = []
        level_num = 0

        while tree_queue:
            
            level_nodes = []
            level_size = len(tree_queue)
            for _ in range(level_size):
                current_node = tree_queue.popleft()        
                if level_num % 2 == 0:
                    level_nodes.append(current_node.val)
                else:
                    level_nodes.insert(0, current_node.val)
                if current_node.left:
                    tree_queue.append(current_node.left)
                if current_node.right:
                    tree_queue.append(current_node.right)
            level_num += 1
            result.append(level_nodes)

        return result
