######### 
#1.
class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size


    def put(self, key, data):
        hash_value = self.hash_function(key, len(self.slots))

        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = data

        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data
            else:
                next_slot = self.rehash(hash_value, len(self.slots))
                while self.slots[next_slot] != None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, len(self.slots))

                if self.slots[next_slot] == None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data

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


###the load factor lambda

#1) 10% => av. number of comparisons = 1.1
#2) 25% => av. number of comparisons = 1.2
#3) 50% => av. number of comparisons = 1.5
#4) 75% => av. number of comparisons = 2.5
#5) 90% => av. number of comparisons = 5.5
#6) 99% => av. number of comparisons = 50.5

#2.

def hash(a_string, table_size):
    sum = 0
    weight = 0
    for pos in range(len(a_string)):
        sum = sum + weight + ord(a_string[pos])
        weight += 1
    return sum % table_size


#3.

def hash1(a_string, table_size):
    sum = 0
    pos = 0
    
    for char in a_string:
        weight = a_string[:pos].count(char)
        sum = sum + weight + ord(char) 
        pos += 1
        

    return sum % table_size
        

my_string = 'aaa'
print(hash1(my_string, 11))

#4.
def hash_w(a_string, table_size):
    sum = 0
    pos = 0
    cur_hash = 0
    for char in a_string:
        weight = a_string[:pos].count(char)
        sum = sum + weight + ord(char) + pos + cur_hash
        pos += 1
        cur_hash += 1
        

    return sum % table_size

print("perf h f")
print(hash_w('apple', 17))
print(hash_w('banana', 17))
print(hash_w('orange', 17))
print(hash_w('tomato', 17))
print(hash_w('pumpkin', 17))









#5.

def bubble_sort(a_list):
    for pass_num in range(len(a_list) - 1, 0, -1):
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp
                print(a_list)

def selection_sort(a_list):
    for fill_slot in range(len(a_list) - 1, 0, -1):
        pos_of_max = 0
        for location in range(1, fill_slot + 1):
            if a_list[location] > a_list[pos_of_max]:
                pos_of_max = location
                

        temp = a_list[fill_slot]
        a_list[fill_slot] = a_list[pos_of_max]
        a_list[pos_of_max] = temp
        
    

def insertion_sort(a_list):
    for index in range(1, len(a_list)):

        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value
        print(a_list)


def shell_sort(a_list):
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        
        print("Afer increments of size", sublist_count, "the list is", a_list)

        sublist_count = sublist_count // 2
        print(a_list)
    
def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = current_value

def merge_sort(a_list):
    print('Splitting ', a_list)
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0       #left half
        j = 0       #right half
        k = 0       #list

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                a_list[k] = left_half[i]

                i += 1
            else:
                a_list[k] = right_half[j]
                j += 1
            
            k += 1

        while i < len(left_half):
            a_list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            a_list[k] = right_half[j]
            j += 1
            k += 1
        
        print('Merging', a_list)
    

import random as rnd


rand_lst = []
for _ in range(11):
    rand_lst.append(rnd.randrange(0, 100))
print('bubble sort')
bubble_sort(rand_lst)
print(rand_lst)
print()
print('selection sort')
selection_sort(rand_lst)
print(rand_lst)
print()
print('insertion sort')
insertion_sort(rand_lst)
print(rand_lst)
print()
print('shell sort')
shell_sort(rand_lst)
print(rand_lst)
print()
print('merge sort')
merge_sort(rand_lst)
print(rand_lst)
print()

#8.

my_char = ['P', 'Y', 'T', 'H', 'O', 'N']
bubble_sort(my_char)
print(my_char)
print()
selection_sort(my_char)
print(my_char)
print()
insertion_sort(my_char)
print(my_char)
print()
shell_sort(my_char)
print(my_char)
print()
merge_sort(my_char)
print(my_char)
print()

 

