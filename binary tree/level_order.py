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
# breadth first 
# time complexity: O(n)

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        array = []
        q= collections.deque()
        q.append(root)
        while q:
            qLen = len(q)
            subArray = []
            for i in range(qLen): # first iteration length is 1[1], second iteration 2[2, 3]
                node = q.popleft()
                subArray.append(node.val)
                if node.left: q.append(node.left)# for every iteration, you enqueue the nodes in each level so next while loop iteration size == # of nodes endqued
                if node.right: q.append(node.right)
            if subArray:
                array.append(subArray# after each for loop iteration, you add the subArray to the larger array
        return array
