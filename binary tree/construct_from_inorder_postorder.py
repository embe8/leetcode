# Problem: Given two lists: inorder (from inorder traversal) and postorder (from postorder traversal)
# build a binary tree (general)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Optimized solution with O(n) time complexity
class Solution(object):
    def buildTree(self, inorder, postorder):
        # root is at the end of postorder list
        self.index = len(postorder) - 1
        # map each element in inorder list to its index
        inorder_index_map = {value: idx for idx, value in enumerate(inorder)}
        # first call to helperf function
        # arguments: postorder array, 0, length of inorder array, hash map of inorder array
        return self.helper(postorder, 0, len(inorder) - 1, inorder_index_map)
        
    def helper(self, postorder, start, end, map):
 
        if start > end: return None
        root_val = postorder[self.index]
        self.index -= 1

        root = TreeNode(root_val)

        inorder_index = map.get(root_val)

        # postorder traversal goes left->right->root
        # but we start building right subtree first before left since we start at the end (root)

        # recursively build right subtree using indices of all elements to the
        # right of the root in the inorder array
        root.right = self.helper(postorder, inorder_index + 1, end, map)
        
        # recursively build left subtree by getting the indices of all elements
        # to the left of the root in the inorder array
        root.left = self.helper(postorder, start, inorder_index - 1, map) 


        return root
