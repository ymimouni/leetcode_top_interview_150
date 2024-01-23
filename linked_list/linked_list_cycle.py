from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            # If fast arrives at the end of the list.
            if not fast or not fast.next:
                return False

            slow = slow.next
            fast = fast.next.next

        return True

#     def hasCycle(self, head: Optional[ListNode]) -> bool:

#         node = head

#         # Map to keep track of visited nodes.
#         visited = set()

#         while node:
#             # If we find a loop, return the position.
#             if node in visited:
#                 print(node)
#                 return True

#             visited.add(node)

#             node = node.next

#         return False

#         node = head
#         # curr_pos = 0

#         # Map to keep track of visited nodes and their positions.
#         visited = {}

#         while node:
#             # If we find a loop, return the position.
#             if node.val in visited:
#                 return visited[node.val]

#             # Add the current node to visited nodes.
#             visited[node.val] = curr_pos

#             node = node.next
#             curr_pos += 1


#         return -1
