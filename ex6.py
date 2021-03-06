#In the hash table map implementation, the hash table size was chosen to be 101. 
# If the table gets full, this needs to be increased. Re-implement the put method so that the table 
# will automatically resize itself when the loading factor reaches a predetermined value 
# (you can decide the value based on your assessment of load versus performance).


class HashTable:
    def __init__(self):
        self.size = 3
        self.slots = [None] * self.size
        self.data = [None] * self.size


    def put(self, key, data):
        hash_value = self.hash_function(key, len(self.slots))

        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] == data   #replace

            else:
                next_slot = self.rehash(hash_value, len(self.slots))
                while self.slots[next_slot] != None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, len(self.slots))
                    if next_slot == hash_value:
                        self.size += 1       
                        self.slots.append(None)
                        self.data.append(None)

                if self.slots[next_slot] == None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data     #replace
            


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


h = HashTable()
h[54] = 'cat'
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
