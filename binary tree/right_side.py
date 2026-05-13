# Problem: Return as a list of integers the node values contained on the right side view of a binary tree
# Approach: use DFS and check when depth equals length of current list (should be 1), append to result list if so

class Solution:
  def rightSide(self, root: Optional [TreeNode])->List[int]:
    res = [] # initialize list to be returned
    def dfs(node, depth):
      if not node: return None
      if depth == len(res): # then it's the first node
        res.append(node.val)
      dfs(node.right, depth + 1)
      dfs(node.left, depth + 1)

    dfs(root, 0)
    return res
