#Using a random number generator, create a list of 500 integers.
# Perform a benchmark analysis using some of the sorting algorithms from this chapter. 
# What is the difference in execution speed?
import random, time

def bubble_sort(a_list):
    for pass_num in range(len(a_list) - 1, 0, -1):
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp

def shell_sort(a_list):
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        
        sublist_count = sublist_count // 2

def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = current_value


def merge_sort(a_list):
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

def quick_sort(a_list):
    quick_sort_helper(a_list, 0, len(a_list) - 1)

def quick_sort_helper(a_list, first, last):
    if first < last:
        split_point = partition(a_list, first, last)

        quick_sort_helper(a_list, first, split_point - 1)
        quick_sort_helper(a_list, split_point + 1, last)

def partition(a_list, first, last):
    pivot_value = a_list[len(a_list)//2]

    left_mark = first + 1 
    right_mark = last

    done = False
    while not done:
        while left_mark <= right_mark and a_list[left_mark] <= pivot_value:
            left_mark = left_mark + 1

        while a_list[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark = right_mark -1 
        
        if right_mark < left_mark:
            done = True

        else:
            temp = a_list[left_mark]
            a_list[left_mark] = a_list[right_mark]
            a_list[right_mark] = temp

    
    temp = a_list[first]
    a_list[first] = a_list[right_mark]
    a_list[right_mark] = temp
    return right_mark



my_testlist = []
for i in range(501):
    my_testlist.append(random.randrange(0, 1000))

my_start = time.time()
bubble_sort(my_testlist)
my_end = time.time()
print("time needed for bubble sort: ", my_end - my_start)

my_testlist1 = []
for i in range(501):
    my_testlist1.append(random.randrange(0, 1000))
my_start = time.time()
shell_sort(my_testlist1)
my_end = time.time()
print('time needed for shell sort: ', my_end - my_start)

my_testlist2 = []
for i in range(501):
    my_testlist2.append(random.randrange(0, 1000))
my_start = time.time()
merge_sort(my_testlist2)
my_end = time.time()
print('time needed for merge sort: ', my_end - my_start)


my_testlist3 = []
for i in range(501):
    my_testlist3.append(random.randrange(0, 1000))
my_start = time.time()
quick_sort(my_testlist3)
my_end = time.time()
print('time needed for quick sort: ', my_end - my_start)


#the slowest sort is bubble sort.
#3 other sort method can show in some cases 0.0 execution time, 
#but in general the time needed is more or less same
