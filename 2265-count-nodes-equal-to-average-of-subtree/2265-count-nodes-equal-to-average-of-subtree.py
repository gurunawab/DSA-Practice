# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def dfs(node):
            if not node: return 0, 0, 0  # (sum, count, matching_nodes)
            l_sum, l_cnt, l_ans = dfs(node.left)
            r_sum, r_cnt, r_ans = dfs(node.right)
            s, c = l_sum + r_sum + node.val, l_cnt + r_cnt + 1
            return s, c, l_ans + r_ans + (s // c == node.val)
        
        return dfs(root)[2]