from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def helper(prev, cur):
            nonlocal n, head
            if not cur:
                return None
            helper(cur, cur.next)
            n -= 1
            if n == 0:
                if not prev:
                    head = cur.next
                else:
                    prev.next = cur.next

        helper(None, head)
        return head
