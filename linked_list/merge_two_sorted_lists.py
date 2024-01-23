from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, p: Optional[ListNode], q: Optional[ListNode]) -> Optional[ListNode]:
        if not p: return q
        if not q: return p
        if p.val <= q.val:
            p.next = self.mergeTwoLists(p.next, q)
            return p
        else:
            q.next = self.mergeTwoLists(p, q.next)
            return q

    # def mergeTwoLists(self, p: Optional[ListNode], q: Optional[ListNode]) -> Optional[ListNode]:
    #     prehead = ListNode()

    #     curr = prehead
    #     while p and q:
    #         if p.val <= q.val:
    #             curr.next = p
    #             p = p.next
    #         else:
    #             curr.next = q
    #             q = q.next
    #         curr = curr.next

    #     curr.next = p if p else q

    #     return prehead.next
