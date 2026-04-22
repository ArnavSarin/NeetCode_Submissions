class Node:
    def __init__(self,key=0,val=0,next = None,prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

        
    def remove(self,node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node


    def move_to_front(self,node):
        front = self.head.next

        self.head.next = node
        node.next = front

        node.prev = self.head
        front.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.move_to_front(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.cache[key] = Node(key,value)
            self.remove(node)
            self.move_to_front(self.cache[key])
            return
        if len(self.cache) == self.capacity:
            node = self.tail.prev
            self.remove(node)
            del self.cache[node.key]
        
        self.cache[key] = Node(key,value)
        self.move_to_front(self.cache[key])
        return




        
