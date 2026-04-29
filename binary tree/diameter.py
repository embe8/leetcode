'''Given a binary tree, return the largest diameter between any two nodes in the tree
where the nodes don not have to include the root
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def helper(root):
            nonlocal res
            if not root: return 0

            leftHeight = helper(root.left)
            rightHeight = helper(root.right)
            res = max(res, leftHeight + rightHeight) # Given tree [1, 2, 3] left subtree height is 1, same as 3, so adding gives two

            return 1 + max(leftHeight, rightHeight)

        helper(root)

        return res
