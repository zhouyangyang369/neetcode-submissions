class ListNode:

    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value

        self.next = None
        self.pre = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        
        self.head = ListNode()
        self.tail = ListNode()

        self.head.next = self.tail
        self.tail.pre = self.head

    def move_to_head(self, node:ListNode):
        node.pre.next = node.next
        node.next.pre = node.pre

        self.insert_to_head(node)

    def insert_to_head(self, node:ListNode):
        node.pre, node.next = self.head, self.head.next
        self.head.next.pre, self.head.next = node, node

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        else:
            self.move_to_head(self.hashmap[key])
            return self.hashmap[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].value = value
            self.move_to_head(self.hashmap[key])
        else:
            self.hashmap[key] = ListNode(key, value)
            self.insert_to_head(self.hashmap[key])
            if len(self.hashmap) > self.capacity:
                removed_node = self.tail.pre
                removed_node.pre.next = self.tail
                self.tail.pre = removed_node.pre
                del self.hashmap[removed_node.key]

            
