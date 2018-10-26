#Implement the selection sort using simultaneous assignment.
import random
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
for _ in range(10):
    my_list.append(random.randrange(0, 100))
    selection_sort(my_list)
    print(my_list)
