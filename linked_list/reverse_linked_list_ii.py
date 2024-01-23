from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        left, tail, right, sub_head = None, head, None, None
        stop = False

        def reverse(prev: ListNode, curr: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
            nonlocal left, tail, right, stop, sub_head

            if n == 0:
                right = curr
                sub_head = prev
                return None

            if m == 1:
                left = prev
                tail = curr

            reverse(curr, curr.next, m - 1, n - 1)

            if prev == left:
                stop = True

            if not stop:
                curr.next = prev

        if not head or not head.next or m == n:
            return head

        reverse(head, head.next, m - 1, n - 1)
        if left:
            left.next = sub_head
        else:
            head = sub_head
        tail.next = right

        return head

    # def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    #     if head is None:
    #         return head

    #     prev, curr = None, head
    #     while left > 1:
    #         prev, curr = curr, curr.next
    #         left, right = left - 1, right - 1

    #     con, tail = prev, curr
    #     while right >= 1:
    #         next = curr.next
    #         curr.next = prev
    #         prev = curr
    #         curr = next
    #         right -= 1

    #     if con:
    #         con.next = prev
    #     else:
    #         head = prev
    #     tail.next = curr

    #     return head

    # def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    #     def reverse(prev: Optional[ListNode], curr: Optional[ListNode]) -> Optional[ListNode]:
    #         if curr.next is None:
    #             curr.next = prev
    #             return curr
    #         next = curr.next
    #         curr.next = prev
    #         return reverse(curr, next)

    #     if not head or not head.next or left == right:
    #         return head

    #     curr = head
    #     while right > 1:
    #         curr = curr.next
    #         right -= 1
    #     right, right_next = curr, curr.next
    #     right.next = None

    #     left_prev = None
    #     curr = head
    #     while left > 1:
    #         left_prev = curr
    #         curr = curr.next
    #         left -= 1
    #     left = curr
    #     if left_prev:
    #         left_prev.next = None

    #     sub_head = reverse(left, left.next)
    #     if left_prev:
    #         left_prev.next = sub_head
    #     else:
    #         head = sub_head
    #     left.next = right_next

    #     return head
