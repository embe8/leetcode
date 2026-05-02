'''given a binary tree, invert it where right and left children of a node are interchanged
and return the root
'''
# Time complexity: O(n)
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        q = deque([root])

        while q:
            node = q.popleft()
            node.left, node.right = node.right, node.left
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)

        return root

