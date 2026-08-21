class Node:

    def __init__(self, key: int, val: int):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None



class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity


        self.left = Node(0,0)
        self.right = Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):

        node.prev.next = node.next
        node.next.prev = node.prev

    def insert_at_end(self, node):

        temp = self.right.prev

        temp.next = node
        node.prev = temp

        self.right.prev = node
        node.next = self.right

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove(node)
        self.insert_at_end(node)

        return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        new_node = Node(key, value)
        self.cache[key] = new_node
        self.insert_at_end(new_node)
        
        if len(self.cache) > self.capacity:
            lru_node = self.left.next
            self.remove(lru_node)
            del self.cache[lru_node.key]