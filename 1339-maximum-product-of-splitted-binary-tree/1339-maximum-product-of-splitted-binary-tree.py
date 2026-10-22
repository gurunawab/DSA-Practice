# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

  def maxProduct(self, root: Optional[TreeNode]) -> int:
    sums = []

    def dfs(node):
      if not node:
        return 0
      s = node.val + dfs(node.left) + dfs(node.right)
      sums.append(s)
      return s

    total = dfs(root)
    return max(s * (total - s) for s in sums) % (10**9 + 7)