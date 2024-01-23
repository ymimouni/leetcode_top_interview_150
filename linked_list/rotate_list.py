from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or not k:
            return head

        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1

        k = k % n
        if not k:
            return head

        new_tail = head
        for _ in range(n - k - 1):
            new_tail = new_tail.next

        old_tail.next = head
        head = new_tail.next
        new_tail.next = None

        return head
