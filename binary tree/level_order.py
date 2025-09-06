from collections import deque

class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []

        result = []
        queue = deque([(root, 0)])  # each item is (node, level)

        while queue:
            node, level = queue.popleft()

            # if this is the first node of a new level, add a new list
            if len(result) <= level:
                result.append([])

            result[level].append(node.val)

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return result
