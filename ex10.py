#A bubble sort can be modiﬁed to “bubble” in both directions. The ﬁrst pass moves “up” the list, 
# and the second pass moves “down.” This alternating pattern continues until no more passes are necessary. 
# Implement this variation and describe under what circumstances it might be appropriate.
def shake_sort(a_list):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(a_list) - 2):
            if a_list[i] > a_list[i + 1]:
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        for i in range(len(a_list) - 2, 0, -1):
            if a_list[i] > a_list[i + 1]:
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
                swapped = True

from random import randrange

lst = []
for _ in range(10):
    lst.append(randrange(0, 1000))
print(lst)
shake_sort(lst)
print(lst)
