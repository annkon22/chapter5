#A bubble sort can be modiﬁed to “bubble” in both directions. The ﬁrst pass moves “up” the list, 
# and the second pass moves “down.” This alternating pattern continues until no more passes are necessary. 
# Implement this variation and describe under what circumstances it might be appropriate.
import random

def bubble_sort(a_list):
    for pass_num in range(len(a_list) - 1, 0, -1):
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
            if a_list[i] < a_list[i - 1] and i != 0:
                a_list[i], a_list[i - 1] = a_list[i - 1], a_list[i]

my_testlist = []
for i in range(21):
    my_testlist.append(random.randrange(0, 1000))

print(my_testlist)
bubble_sort(my_testlist)
print(my_testlist)