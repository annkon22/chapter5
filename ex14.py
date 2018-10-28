#One way to improve the quick sort is to use an insertion sort on lists that have a small length 
# (call it the “partition limit”). Why does this make sense? Re-implement the quick sort and use it to sort a random list of integers. 
# Perform an analysis using different list sizes for the partition limit
import random



def quick_sort(a_list):
    partition_limit = 10
    if len(a_list) > partition_limit:
        quick_sort_helper(a_list, 0, len(a_list) - 1)
    else:
        insertion_sort(a_list)
        
def quick_sort_helper(a_list, first, last):
    if first < last:
        split_point = partition(a_list, first, last)

        quick_sort_helper(a_list, first, split_point - 1)
        quick_sort_helper(a_list, split_point + 1, last)

def median(a_list, first, middle, last):
    if a_list[first] < a_list[last]:
        return first if a_list[middle] < a_list[first] else middle if a_list[middle] < a_list[last] else last
    else:
        return last if a_list[middle] < a_list[last] else middle if a_list[middle] < a_list[first] else first


def partition(a_list, first, last):

    pivotindex = median(a_list, first, (first + last) // 2, last)
    a_list[first], a_list[pivotindex] = a_list[pivotindex], a_list[first]
    pivot_value = a_list[first]
    

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

def insertion_sort(a_list):
    for index in range(1, len(a_list)):

        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value

my_list = []
for i in range(20):
    my_list.append(random.randrange(0, 100))
quick_sort(my_list)
print(my_list)