class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)  # dummy nodes
        self.left.next, self.right.prev = self.right, self.left

    # left and right nodes are dummies,
    # so insert before the right node
    def insert(self, node: Node):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.next, node.prev = next, prev

    # remove element by dropping ref
    def remove(self, node: Node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def get(self, key: int) -> int:
        # if the key exists, remove it and move it to the right side.
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # if the key already exists, remove it.
        if key in self.cache:
            self.remove(self.cache[key])
        # crete a new node and insert it.
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        # when inserting a key, if the cache exceeds the capacity,
        # remove the LRU key from cache and from linked list
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
