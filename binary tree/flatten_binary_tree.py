'''
Given the root of a binary tree, flatten it to a linked list
where all left children are null and all elements are in the right subtree
'''
# approach is python version of the suggested solution in the site's discussion
# uses a reversed postorder traversal right->left->root
class Solution(object):
    def __init__(self):
        self.prev = None

    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None
        """
        if not root:
            return
        self.flatten(root.right)
        self.flatten(root.left)
        # we essentially build the linked tree backwards
        # set the current node's right child to the prev node
        root.right = self.prev # right child of 5 becomes previously visited 6 so 5->6
        # all left children needs to be empty
        root.left = None # 5 left child becomes null
        # to prepare for connection of next nodes
        # we set the prev pointer to the current node
        self.prev = root # set prev as 5
