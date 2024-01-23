from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pre_head = ListNode()
        curr = pre_head

        carry = 0
        while l1 is not None or l2 is not None or carry != 0:
            l1_val = l1.val if l1 is not None else 0
            l2_val = l2.val if l2 is not None else 0
            num = l1_val + l2_val + carry
            val, carry = num % 10, num // 10
            curr.next = ListNode(val)
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            curr = curr.next

        return pre_head.next

    # def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    #     pre_head = ListNode()
    #     curr = pre_head

    #     ret = 0
    #     while l1 and l2:
    #         num = l1.val + l2.val + ret
    #         val, ret = num % 10, num // 10
    #         curr.next = ListNode(val)
    #         l1, l2, curr = l1.next, l2.next, curr.next

    #     p = l1 if l1 is not None else l2
    #     while p:
    #         num = p.val + ret
    #         val, ret = num % 10, num // 10
    #         curr.next = ListNode(val)
    #         p, curr = p.next, curr.next

    #     if ret != 0:
    #         curr.next = ListNode(ret)

    #     return pre_head.next
