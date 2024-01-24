# from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        leftmost = root
        while leftmost:
            cur = leftmost
            leftmost = None
            while cur:
                if cur.left:
                    if leftmost:
                        right = cur.left
                        left.next = right
                    else:
                        leftmost = cur.left
                    left = cur.left
                if cur.right:
                    if leftmost:
                        right = cur.right
                        left.next = right
                    else:
                        leftmost = cur.right
                    left = cur.right
                cur = cur.next

        return root

    # def connect(self, root: 'Node') -> 'Node':
    #     if not root:
    #         return root
    #
    #     queue = deque([root])
    #
    #     while queue:
    #         n = len(queue)
    #         for idx in range(n):
    #             cur = queue.popleft()
    #             if idx < n - 1:
    #                 cur.next = queue[0]
    #             if cur.left:
    #                 queue.append(cur.left)
    #             if cur.right:
    #                 queue.append(cur.right)
    #
    #     return root
