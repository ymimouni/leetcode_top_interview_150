from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse(self, node: Optional[ListNode]) -> Optional[ListNode]:
        if not node or not node.next:
            return node

        new_head = self.reverse(node.next)
        node.next.next = node
        node.next = None
        return new_head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)

        con = dummy
        cur = tail = head
        i = 1
        while cur:
            while cur and i < k:
                cur = cur.next
                i += 1
            if cur:
                next_head = cur.next
                cur.next = None
                tail = con.next
                p = self.reverse(con.next)
                if con.next == head:
                    head = p
                else:
                    con.next = p
                tail.next = next_head
                con = tail
                cur = next_head
                i = 1

        return head
