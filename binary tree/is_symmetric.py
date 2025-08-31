'''
Checks if the binary tree is symmetric
Symmetric: left and right subtrees are mirror images of each other
'''
# Recursive solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def helper(leftSubtree, rightSubtree):
            if not leftSubtree and not rightSubtree:
                return True

            if not leftSubtree or not rightSubtree:
                return False
            if leftSubtree.val != rightSubtree.val:
                return False
            return helper(leftSubtree.left, rightSubtree.right) and helper(leftSubtree.right, rightSubtree.left)
        # if tree is empty
        if not root:
            return True
        return helper(root.left, root.right)

# Iterative solution
class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        q1 = [root.left]
        q2 = [root.right]
        while q1 and q2:
            leftSubtree = q1.pop(0)
            rightSubtree = q2.pop(0)
            
            if not leftSubtree and not rightSubtree:
                continue
            if not leftSubtree or not rightSubtree:
                return False
            if leftSubtree.val != rightSubtree.val:
                return False
            q1.append(leftSubtree.left)
            q2.append(rightSubtree.right)
            q1.append(leftSubtree.right)
            q2.append(rightSubtree.left)
        return True
        
        

