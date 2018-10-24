#Set up a random experiment to test the difference between a sequential search 
# and a binary search on a list of integers. Use the binary search functions given in the text
#(recursive and iterative). Generate a random,ordered list of integers and do abenchmark analysis for each one. 
# What are your results? Can you explain them?

import random, string, time


def sequential_search(a_list, item):
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos += 1
    return found


def binary_search(a_list, item):
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found

def binary_search_recurive(a_list, item):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
    
    if a_list[midpoint]  == item:
        return True
    else:
        if item < a_list[midpoint]:
            return binary_search(a_list[:midpoint], item)
        else:
            return binary_search(a_list[midpoint + 1:], item)


def bubble_sort(a_list):
    for pass_num in range(len(a_list) - 1, 0, -1):
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp
        
        

def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

my_word = randomword(100)
print(my_word)

my_lst_str = []
for char in my_word:
    my_lst_str.append(char)


my_start = time.time()
print(sequential_search(my_lst_str, 'h'))
my_end = time.time()
print("time needed for seq search: ", my_end - my_start)

my_start = time.time()
bubble_sort(my_lst_str)
print("list after sorting", my_lst_str)
print(binary_search(my_lst_str, 'h'))
my_end = time.time()
print("time needed for binary search: ", my_end - my_start)

my_word1 = randomword(100)
print(my_word1)

my_lst_str1 = []
for char in my_word1:
    my_lst_str1.append(char)
my_start = time.time()
bubble_sort(my_lst_str1)
print(binary_search_recurive(my_lst_str1, 'h'))
my_end = time.time()
print("time needed for binary recursive search: ", my_end - my_start)

