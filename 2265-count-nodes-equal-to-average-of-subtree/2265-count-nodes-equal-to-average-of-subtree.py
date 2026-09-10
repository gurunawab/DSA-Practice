# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.matching_nodes = 0

        def traverse(node):
            if not node:
                return (0, 0)  # (sum, count)

            left_sum, left_count = traverse(node.left)
            right_sum, right_count = traverse(node.right)

            current_sum = left_sum + right_sum + node.val
            current_count = left_count + right_count + 1

            # Check integer division (rounded down)
            if current_sum // current_count == node.val:
                self.matching_nodes += 1

            return (current_sum, current_count)

        traverse(root)
        return self.matching_nodes