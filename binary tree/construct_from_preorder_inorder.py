# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Bad solution with O(n^2) time complexity
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not preorder or not inorder:
            return None

        # First element in preorder is the root
        root_val = preorder[0]
        root = TreeNode(root_val)

        # Find the index of the root in inorder
        mid = inorder.index(root_val)

        # Recursively build left and right subtrees
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root

# Optimized solution with O(n) time complexity








        
