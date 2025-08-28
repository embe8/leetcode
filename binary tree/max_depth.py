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
