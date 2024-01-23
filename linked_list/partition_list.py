from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)

        cur = head
        while cur:
            if cur.val < x:
                before.next = cur
                before = cur
            else:
                after.next = cur
                after = cur
            cur = cur.next

        after.next = None
        before.next = after_head.next
        return before_head.next
