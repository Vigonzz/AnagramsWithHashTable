# Violet Gonzalaz, octobr 23, 2026

# Task 1: 
# implement a Hash data structure from scratch. You can’t use built-in Hash or Dictionary APIs. You can use a 
# built-in Array or List or your custom-built LinkedList.  The Hash class must have the following functions and fields - 
# hashtable, hash(x), insert(x), size()
# small debugging, questions about implementations and overall help with structure were assisted with claude chat:
# https://claude.ai/share/7a85c04f-86cc-4347-8c54-ddc88be4bf2b
# ALL code was produced by myself 

# Additional reading on open addressing vs separate chaining, and overall hashing:
# Scribd. (n.d.). Scribd. https://www.scribd.com/document/623871691/Hashing 
# https://namir.dev/blog/open-addressing-vs-chaining-hash-collisions/
# GeeksforGeeks. (2025b, July 23). Implementation of hash table in Python using separate chaining. https://www.geeksforgeeks.org/dsa/implementation-of-hash-table-in-python-using-separate-chaining/ 



# Create the node
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


class HashTable:

    # Set up the hashtable
    def __init__(self, table_size = 7307):
        self.table_size = table_size
        self.table = [None] * table_size
        self.counter = 0

    # Our hash  method that will return the integers index
    def hash(self, x):
        running_total = 0
        for character in x:
          # I had looked at references for ord since I was new to the concept 
          # Vultr. (2024, September 27). Python ord() - convert character to integer. Vultr Docs. https://docs.vultr.com/python/built-in/ord 
          # GeeksforGeeks. (2025a, April 27). Ord() function in Python. https://www.geeksforgeeks.org/python/ord-function-python/ 
          running_total = (running_total * 31) + ord(character)
        return running_total % self.table_size
    
    # Insert method that will allow us to insert words into our hash table  
    def insert(self, x):
        index = self.hash(x)
        current = self.table[index]

        while current is not None:
            if current.key == x:
                return False
            else:
                current = current.next

        new_node = Node(x)
        new_node.next = self.table[index]
        self.table[index] = new_node
        self.counter += 1

        return True

    def size(self):
        return self.counter

    
