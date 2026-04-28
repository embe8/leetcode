# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Checks if two trees are the same/contain the same elements, the idea is if two trees are empty, they're the same
Else check if first node is the same, if so proceed with passing both left and right nodes of each tree
Else if not same, return false
'''
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """

        def helper(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return helper(p.left, q.left) and helper(p.right, q.right)
        return helper(p, q)

# without helper function, recursive
# Time complexity: O(n)
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else: return False

# depth first search
# time complexity: O(n)
# left most nodes first are checked then right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode])->bool:
        stack = [(p, q)]

        while stack:
            node1, node2 = stack.pop()
            if not node1 and not node2: continue
            if not node1 or not node2 or node1.val != node2.val:
                return False
            stack.append((node1.right, node2.right))
            stack.append((node1.left, node2.left)) 
        return True



