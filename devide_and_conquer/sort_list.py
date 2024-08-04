from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.tail = None
        self.next_sublist = None

    def length(self, node: Optional[ListNode]) -> int:
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    def split(self, start: Optional[ListNode], size: int) -> Optional[ListNode]:
        mid_prev = start
        end = start.next
        i = 1
        while i < size and (mid_prev.next is not None or end.next is not None):
            if end.next is not None:
                end = end.next.next if end.next.next else end.next
            mid_prev = mid_prev.next
            i += 1

        mid = mid_prev.next
        mid_prev.next = None
        self.next_sublist = end.next
        end.next = None
        return mid

    def merge(self, p: Optional[ListNode], q: Optional[ListNode]) -> Optional[ListNode]:
        curr = dummy = ListNode()

        while p and q:
            if p.val <= q.val:
                curr.next = p
                p = p.next
            else:
                curr.next = q
                q = q.next
            curr = curr.next

        curr.next = p if p else q

        while curr.next:
            curr = curr.next

        self.tail.next = dummy.next
        self.tail = curr
        return None

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        n = self.length(head)
        start = head

        size = 1
        dummy_head = ListNode()
        while size < n:
            self.tail = dummy_head
            while start is not None:
                if start.next is None:
                    self.tail.next = start
                    break
                mid = self.split(start, size)
                self.merge(start, mid)
                start = self.next_sublist
            size *= 2
            start = dummy_head.next

        return dummy_head.next

# class Solution:
#     def merge(self, p: Optional[ListNode], q: Optional[ListNode]) -> Optional[ListNode]:
#         curr = dummy = ListNode()

#         while p and q:
#             if p.val <= q.val:
#                 curr.next = p
#                 p = p.next
#             else:
#                 curr.next = q
#                 q = q.next
#             curr = curr.next

#         curr.next = p if p else q
#         return dummy.next


#     def get_middle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         slow = fast = head
#         prev = None

#         while fast and fast.next:
#             prev = slow
#             slow, fast = slow.next, fast.next.next

#         if prev:
#             prev.next = None

#         return slow

#     def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head or not head.next:
#             return head
#         middle = self.get_middle(head)
#         left = self.sortList(head)
#         right = self.sortList(middle)
#         return self.merge(left, right)
