#Implement the merge_sort function without using the slice operator.
import random

def merge_sort(a_list):
    if length(a_list) <= 1:
        return a_list
    else:
        middle = len(a_list) // 2
        left = [i for i in range(0, middle - 1)
        right = [i for i in range(middle, len(a_list))

        left = merge_sort(left)
        right = merge_sort(right)

        if left[len(left)] <= right[0]:
            left.append(right)
            return left
        result = _merge(left, right)
        return(result)

def _merge(left, right):
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left[0].remove()
        else:
            result.append(right[0])
            right[0].remove()
    if len(left) > 0:
        result.append(left)
    if len(right) > 0:
        result.append(right)
    return result


my_list = []
for i in range(10):
    my_list.append(random.randrange(0, 100))

merge_sort(my_list)
print(my_list)
 


