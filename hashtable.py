# Violet Gonzalaz, octobr 23, 2026

# Task 1: 
# implement a Hash data structure from scratch. You can’t use built-in Hash or Dictionary APIs. You can use a 
# built-in Array or List or your custom-built LinkedList.  The Hash class must have the following functions and fields - 
# hashtable, hash(x), insert(x), size()


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
          running_total = (running_total * 31) + ord(character)
        return running_total % self.table_size
    
    # Insert method that
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

    def size(self):
        return self.counter

    
test_table = HashTable(11)
print(test_table.hash("dna"))