#Implement the merge_sort function without using the slice operator.
import random

def merge_sort(a_list):
    if len(a_list) <= 1:
        return a_list

    left = []
    right = []
    for i in range(len(a_list)):
        if i < len(a_list) // 2:
            left.append(a_list[i])
        else:
            right.append(a_list[i])

    left = merge_sort(left)
    right = merge_sort(right)

    return _merge(left, right)

def _merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))            
        else:
            result.append(right.pop(0))            

    while len(left) > 0:
        result.append(left.pop(0))
    while len(right) > 0:
        result.append(right.pop(0))
    return result


my_list = []
for i in range(10):
    my_list.append(random.randrange(0, 100))
print(my_list)
print(merge_sort(my_list))
