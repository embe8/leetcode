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
class Solution(object):
    def buildTree(self, preorder, inorder):
        self.index = 0
        inorder_index_map = {value: idx for idx, value in enumerate(inorder)}
        return self.helper(preorder, 0, len(inorder) - 1, inorder_index_map)
        
    def helper(self, preorder, start, end, map):
        if start > end: return None
        root_val = preorder[self.index]
        self.index += 1

        root = TreeNode(root_val)

        inorder_index = map.get(root_val)
        
        # recursively build left subtree by getting the indices of all elements
        # to the left of the root in the inorder array
        root.left = self.helper(preorder, start, inorder_index - 1, map) 
        # recursively build right subtree using indices of all elements to the
        # right of the root in the inorder array
        root.right = self.helper(preorder, inorder_index + 1, end, map)

        return root






        
