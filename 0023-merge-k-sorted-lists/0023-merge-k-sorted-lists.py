# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        nodes = []
        for l in lists:
            while l:
                nodes.append(l)
                l = l.next
        nodes.sort(key=lambda x: x.val)
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        if nodes:
            nodes[-1].next = None
        return nodes[0] if nodes else None