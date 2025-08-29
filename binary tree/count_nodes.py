# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Returns the number of complete nodes in a binary tree
Complete nodes = with both left and right children
'''
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
