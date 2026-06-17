class Node:
    def __init__(self, key, value):
        #Set up the node data structure to traverse elements 
        #with the linked list 
        self.key = key
        self.value = value 
        self.next = self.prev = None 


class LRUCache:

    def __init__(self, capacity: int):
        #set up the cache 
        #set up LRU and MRU 
        #wire up the pointers 
        self.cache = {}
        self.cap = capacity

        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left 
        
    def insert(self, node):
        #We insert in self.right
        #this is because it is MRU 
        #Most Recently Used 
        prev = self.right.prev
        nxt = self.right 

        #Wire up node 
        node.next = nxt
        node.prev = prev 

        #Connect it to the list 
        prev.next = node
        nxt.prev = node 

    
    def remove(self, node):
        #Store the nodes prev and next pointers 
        prev = node.prev 
        nxt = node.next 

        #then overwrite by connecting the two pointers 

        prev.next = nxt
        nxt.prev = prev 


    def get(self, key: int) -> int:
        #Check if the key is in the cache 
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            #We remove and insert to ensure it belongs in the MRU
            return self.cache[key].value
        return -1 
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            #If key is present in cache we need to remove it 
            #so that way we can store the next value 
        self.cache[key] = Node(key, value)
        #Associate key with the new node
        self.insert(self.cache[key])
        #insert into list 

        if len(self.cache) > self.cap:
            #if list's length is above the capacity 
            #then we remove node then key 
            lru = self.left.next 
            self.remove(lru)
            del self.cache[lru.key]
            #remove the key from the cache 
        
        
        
