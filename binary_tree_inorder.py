class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None
    # Recursive solution
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        left_subtree = self.inorderTraversal(root.left)
        current = [root.val]
        right_subtree = self.inorderTraversal(root.right)

        return left_subtree + current + right_subtree


    def insertNode(self, value):
        new_node = TreeNode(value)
        if self.root is None:
            self.root = new_node
            return

        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if not current.left:
                current.left = new_node
                return
            else:
                queue.append(current.left)

            if not current.right:
                current.right = new_node
                return
            else:
                queue.append(current.right)

if __name__ == "__main__":
    # Create binary tree:
    btree = BinaryTree()
    insert_list = [1, 2, 3, 5, 4, 6, 7]
    for value in insert_list:
        btree.insertNode(value)

    print("\nTree after insertion:")
    print(btree.inorderTraversal(btree.root))