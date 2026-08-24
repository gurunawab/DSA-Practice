# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def createBinaryTree(
        self, descriptions: List[List[int]]
    ) -> Optional[TreeNode]:
        nodes, children = {}, set()

        for p, c, is_left in descriptions:
            parent = nodes.setdefault(p, TreeNode(p))
            child = nodes.setdefault(c, TreeNode(c))
            if is_left:
                parent.left = child
            else:
                parent.right = child
            children.add(c)

        root_val = (set(nodes) - children).pop()
        return nodes[root_val]