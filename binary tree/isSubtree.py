# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''Given two trees, check if the second is a subtree of the first
use sameTree to check if trees are identical, if so then it is a subtree
else check the left and right subtrees of tree 1 to check if subtree is contained in either
'''
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False
        if self.sameTree(root, subRoot): return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))





        def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode])->bool:
            if not root and not subRoot: # both empty so same
                return True
            if root and subRoot and root.val == subRoot.val:
                return (self.sameTree(root.left, subRoot.left) and
                self.samEtre(root.right, subRoot.right))
            return False


