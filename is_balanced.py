class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None
      
    # Recursive solution
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        Returns True if tree is balanced else returns False
        where for False, check_height() returns -1 meaning tree is unbalanced 
        """
        def check_height(node):
            """
            :type root: Optional[TreeNode]
            :rtype: bool
            Traverses left subtree, returning its height
            and then traverses the right subtree, returning its height
            lastly, gets the difference between the two heights
            """
            if not node or node.val is None:
                print("zero")
                return 0  # Base case: height of empty tree is 0
            left = check_height(node.left)

            if left == -1:
                return -1  # Left subtree is not balanced
            right = check_height(node.right)
            if right == -1:
                return -1  # Right subtree is not balanced

            if abs(left - right) > 1:
                return -1  # Not balanced at this node
            return max(left, right) + 1  # Return height
        return check_height(root) != -1
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        Prints the tree's left subtree first, root, then right subtree
        Since it's a binary tree (not bst) values are not printed in
        ascending order
        """
        if not root:
            return []
        left_subtree = self.inorderTraversal(root.left)
        current = [root.val]
        right_subtree = self.inorderTraversal(root.right)

        return left_subtree + current + right_subtree


    def insertNode(self, value):
        new_node = TreeNode(value)
        if not self.root:
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
    # Create binary trees:
    btree1 = BinaryTree()
    btree2 = BinaryTree()
    insert_list1 = [1,2,2,3,3,None,None,4,4]
    insert_list2 = [1, 2, 3]

    for value in insert_list1:
        btree1.insertNode(value)
    for value in insert_list2:
        btree2.insertNode(value)
    print("\nTree1 after insertion:")
    print(btree1.inorderTraversal(btree1.root))
    print("\nTree2 after insertion:")
    print(btree2.inorderTraversal(btree2.root))

    print("\nCheck if trees are balanced:")
    print(btree1.isBalanced(btree1.root))
    print(btree2.isBalanced(btree2.root))

