class Node:
    def __init__(self, key: int = 0, value: int = 0, next: Node = None, prev: Node = None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

class LRUCache:
    '''
    Hashmap + doubly linked list

    Hashmap: key -> node 

    Doubly linked list: head <-> least recently used ... most recently used <-> tail

    Always append to tail.prev 

    Always delete from head.next

    Keep track of: 
    - max capacity
    '''
    def __init__(self, capacity: int):
        self.max_capacity = capacity
        self.key_to_node = {}
        self.head = Node()
        self.tail = Node(prev=self.head)
        self.head.next = self.tail

    def _remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert(self, node: Node) -> None:
        self.tail.prev.next = node
        node.prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail
        
    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1

        # get the key
        node = self.key_to_node[key]

        self._remove(node)
        self._insert(node)
        return node.value

         
    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.value = value

            self._remove(node)
            self._insert(node)
            return

        node = Node(key=key, value=value)
        self.key_to_node[key] = node
        self._insert(node)

        # handle eviction
        if len(self.key_to_node) > self.max_capacity:
            lru_key = self.head.next.key
            self._remove(self.head.next)
            del self.key_to_node[lru_key]


        
