#Implement the binary search using recursion without the slice operator. 
# Recall that you will need to pass the list along with the starting and ending 
# index values for the sublist. Generate a random, ordered list of integers and do a benchmark analysis

import random, time

def binary_search_recurive(a_list, first, last, item):
    
    found = False
    midpoint = (first + last) // 2
    if midpoint == 0 or midpoint == len(a_list) - 1 and not found:
        return "no such number"
    if a_list[midpoint] == item:
        found = True
    else:
        if item < a_list[midpoint]:   
            last = midpoint - 1    
            return binary_search_recurive(my_list, first, last, item)
        else:
            first = midpoint + 1
            return binary_search_recurive(my_list, first, last, item)
    return found

def selection_sort(a_list):
    for fill_slot in range(len(a_list) - 1, 0, -1):
        pos_of_max = 0
        for location in range(1, fill_slot + 1):
            if a_list[location] > a_list[pos_of_max]:
                pos_of_max = location

        temp = a_list[fill_slot]
        a_list[fill_slot] = a_list[pos_of_max]
        a_list[pos_of_max] = temp


my_list = []
for i in range(10):
    my_list.append(random.randrange(0, 100))
selection_sort(my_list)
print(my_list)



my_start = time.time()
my_first = 0
my_last = len(my_list) - 1
print(binary_search_recurive(my_list, my_first, my_last, 5))
my_end = time.time()
print('Time needed for this search: ', my_end - my_start)
