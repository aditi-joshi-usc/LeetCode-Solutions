class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:


    def __init__(self, capacity: int):
        
        self.head = Node(-1,-1)
        self.tail = Node(-1, -1)
        self.tail.prev = self.head
        self.head.next = self.tail
        self.capacity = capacity

        self.node_dict = {}

    def get(self, key: int) -> int:
        if key not in self.node_dict:
            return -1
        node = self.node_dict[key]
        self.remove_node(node)
        self.add_node(node)

        return node.value

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def add_node(self, node):
        tail_prev = self.tail.prev
        tail_prev.next = node
        node.prev = tail_prev
        node.next = self.tail
        self.tail.prev = node


    def put(self, key: int, value: int) -> None:
        if key in self.node_dict:
            self.remove_node(self.node_dict[key])
        
        new_node = Node(key, value)
        self.add_node(new_node)
        self.node_dict[key] = new_node
        if len(self.node_dict) > self.capacity:
            del_node = self.head.next
            self.remove_node(del_node)
            del self.node_dict[del_node.key]


      




# def __init__(self, capacity: int):
#         self.lru_dict = dict()
#         self.size = capacity
#         self.lru = []

#     def get(self, key: int) -> int:
#         if key in self.lru_dict:
#             self.lru.remove(key)
#             self.lru.append(key)
#             return self.lru_dict[key] 
#         else:
#             return -1

#     def put(self, key: int, value: int) -> None:
#         if key in self.lru_dict:
#             self.lru_dict[key] = value
#             self.lru.remove(key)
#             self.lru.append(key)
            
#         else:
#             if len(self.lru_dict) >= self.size:
#                 del self.lru_dict[self.lru[0]]
#                 self.lru.pop(0)
#             self.lru_dict[key] = value
#             self.lru.append(key)
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)