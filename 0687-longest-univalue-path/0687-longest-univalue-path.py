# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            l, r = dfs(node.left), dfs(node.right)
            left_arrow = (
                l + 1 if node.left and node.left.val == node.val else 0
            )
            right_arrow = (
                r + 1 if node.right and node.right.val == node.val else 0
            )
            ans = max(ans, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)

        dfs(root)
        return ans