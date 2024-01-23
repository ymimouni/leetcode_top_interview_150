class DLNode:
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        self.map_ = {}
        self.capacity = capacity
        self.size = 0
        self.head, self.tail = DLNode(), DLNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node: DLNode) -> None:
        """
        Always add the new node right after the head.
        """
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: DLNode) -> None:
        prev, next_ = node.prev, node.next

        prev.next = next_
        next_.prev = prev

    def _move_to_head(self, node: DLNode) -> None:
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self) -> DLNode:
        node = self.tail.prev
        self._remove_node(node)
        return node

    def get(self, key: int) -> int:
        if key not in self.map_:
            return -1

        # Move the accessed node to the head.
        self._move_to_head(self.map_[key])

        return self.map_[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.map_:
            self.map_[key].val = value
            # Move the node to the head.
            self._move_to_head(self.map_[key])
        else:
            # Create a new node and add it to the list.
            node = DLNode(key=key, val=value)
            self.map_[key] = node
            self._add_node(node)
            self.size += 1

            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.map_[tail.key]
                self.size -= 1


# from collections import OrderedDict


# class LRUCache(OrderedDict):

#     def __init__(self, capacity: int):
#         self.capacity = capacity

#     def get(self, key: int) -> int:
#         if key not in self:
#             return -1

#         self.move_to_end(key)
#         return self[key]


#     def put(self, key: int, value: int) -> None:
#         if key in self:
#             self.move_to_end(key)
#         self[key] = value
#         if len(self) > self.capacity:
#             self.popitem(last=False)
