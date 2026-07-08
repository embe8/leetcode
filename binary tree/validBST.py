# return True if given binary search tree is valid: for it to be valid, all left children should be less than its parent
# all right children should be more than its parent
# both left and right subtrees are also binary trees

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False
            
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)

        return valid(root, float("-inf"), float("inf"))
