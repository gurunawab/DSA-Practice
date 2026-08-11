# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node, go_left, steps):
            if not node:
                return steps - 1
            if go_left:
                return max(dfs(node.left, False, steps + 1), dfs(node.right, True, 1))
            return max(dfs(node.right, True, steps + 1), dfs(node.left, False, 1))

        return dfs(root, True, 0)