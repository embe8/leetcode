'''
Given the root of the binary tree and integer value
representing the index of smallest element, return the value
of the nth smallest element
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Uses inorder traversal to return the elements listed
in ascending order returns the value of the kth element
according to the index
'''
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        if not root: return None
        # traverse in order
        inorder_list = []
        def inorder(node):
            # stop traversal if reached leaf node
            if not node: return None
            # traverse left subtree
            inorder(node.left)
            # place node root value in list
            inorder_list.append(node.val)
            # traverse right subtree
            inorder(node.right)
        # recursive call to helper function
        inorder(root)
        return inorder(inorder_list[k - 1])
        

        
