#5. How can you delete items from a hash table that uses chaining for collision resolution? 
# How about if open addressing is used? What are the special circumstances that must be handled? 
# Implement the del method for the HashTable class.

class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [[] for _ in range(self.size)]


    def put(self, key, data):
        hash_value = self.hash_function(key, len(self.slots))

        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value].append(data)
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value].append(data)

    def hash_function(self, key, size):
        return key % size

    def rehash(self, old_hash, size):
        return (old_hash + 1) % size

    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = start_slot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)
    
    def __setitem__(self, key, data):
        self.put(key, data)

    def remove(self, key, data):
        hash_value = self.hash_function(key, len(self.slots))
        if self.slots[hash_value] == None:
            return
        else:
            self.slots[hash_value] = None
            self.data[hash_value].remove(data)




    
h = HashTable()
h[54] = 'cat'
h[54] = 'tomato'

h[26] = 'dog'
h[93] = 'lion'
h[17] = 'tiger'
h[77] = 'bird'
h[31] = 'cow'
h[44] = 'goat'
h[55] = 'pig'
h[20] = 'chicken'

print(h.slots)
print(h.data)
print()
h.remove(54, 'tomato')
print(h.data)
