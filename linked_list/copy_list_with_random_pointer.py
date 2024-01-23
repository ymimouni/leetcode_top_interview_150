class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        # Creating a new weaved list of original and copied nodes.
        ptr = head
        while ptr:
            # Cloned node.
            new_node = Node(ptr.val, None, None)

            # Inserting the cloned node just next to the original node.
            new_node.next = ptr.next
            ptr.next = new_node
            ptr = new_node.next

        # Now link the random nodes of the new nodes created.
        ptr = head

        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next

        # Unweave the linked list to get back the original linked list and the cloned list.
        old_list_ptr = head
        new_list_ptr = head.next
        new_head = head.next
        while old_list_ptr:
            old_list_ptr.next = old_list_ptr.next.next
            new_list_ptr.next = new_list_ptr.next.next if new_list_ptr.next else None
            old_list_ptr = old_list_ptr.next
            new_list_ptr = new_list_ptr.next

        return new_head

#     def __init__(self):
#         # Dictionary that holds old nodes as keys and new nodes as values.
#         self.visitedNodes = {}

#     def getClonedNode(self, node):
#         if node:
#             # Check if it's in the visited dictionary.
#             if node in self.visitedNodes:
#                 return self.visitedNodes[node]
#             else:
#                 # Create a new node, save the reference in the visited dictionary and return it.
#                 self.visitedNodes[node] = Node(node.val, None, None)
#                 return self.visitedNodes[node]
#         return None

#     def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
#         if not head:
#             return None

#         old_node = head

#         # Creating the new node.
#         new_node = Node(old_node.val, None, None)

#         self.visitedNodes[old_node] = new_node

#         # Iterate on the linked list until all nodes are clones.
#         while old_node:
#             # Get the clones of the nodes referenced by random and next pointers.
#             new_node.next = self.getClonedNode(old_node.next)
#             new_node.random = self.getClonedNode(old_node.random)

#             # Move one step ahead in the linked list.
#             old_node = old_node.next
#             new_node = new_node.next

#         return self.visitedNodes[head]

#     def __init__(self):
#         # Dictionary that holds old nodes as keys and new nodes as values.
#         self.visitedNodes = {}

#     def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
#         if not head:
#             return None

#         # If we have already visited the current node, then we simply return the cloned version.
#         if head in self.visitedNodes:
#             return self.visitedNodes[head]

#         # Create a new node.
#         node = Node(head.val, None, None)

#         # Save this value in the hashmap. This is needed since there might be loops during traversal.
#         self.visitedNodes[head] = node

#         # Recursively copy the remaining linked list.
#         node.next = self.copyRandomList(head.next)
#         node.random = self.copyRandomList(head.random)

#         return node
