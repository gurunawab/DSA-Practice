# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaves(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [root.val]
            return get_leaves(root.left) + get_leaves(root.right)
            
        return get_leaves(root1) == get_leaves(root2)