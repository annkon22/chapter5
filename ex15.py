#Implement the median-of-three method for selecting a pivot value as a modiﬁcation to quick_sort. 
# Run an experiment to compare the two techniques.
import random
def quick_sort(a_list):
    quick_sort_helper(a_list, 0, len(a_list) - 1)

def quick_sort_helper(a_list, first, last):
    if first < last:
        split_point = partition(a_list, first, last)

        quick_sort_helper(a_list, first, split_point - 1)
        quick_sort_helper(a_list, split_point + 1, last)

def partition(a_list, first, last):

    a, b, c = first, (first + last) // 2, last

    if a_list[a] > a_list[b]:
        if a_list[a] < a_list[c]:
            pivot_value = a_list[a]
        elif a_list[b] > a_list[c]:
            pivot_value = a_list[b]
        else:
            pivot_value = a_list[c]
    else:
        if a_list[a] > a_list[c]:
            pivot_value = a_list[a]
        elif a_list[b] < a_list[c]:
            pivot_value = a_list[b]
        else:
            pivot_value = a_list[c]

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


my_list = []
for i in range(200):
    my_list.append(random.randrange(0, 100))
quick_sort(my_list)
end = time.time()
print(my_list)
