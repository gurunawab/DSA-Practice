# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        crit = []
        prev, curr, i = head, head.next if head else None, 1

        while curr and curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or (curr.val < prev.val and curr.val < curr.next.val):
                crit.append(i)
            prev, curr, i = curr, curr.next, i + 1

        if len(crit) < 2:
            return [-1, -1]

        min_d = min(crit[j] - crit[j - 1] for j in range(1, len(crit)))
        max_d = crit[-1] - crit[0]
        
        return [min_d, max_d]