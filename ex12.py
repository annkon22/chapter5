#Perform a benchmark analysis for a shell sort, using different increment sets on the same list.
import time, random
def shell_sort(a_list):
    sublist_count = len(a_list) // 3
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        
        print("Afer increments of size", sublist_count, "the list is", a_list)

        sublist_count = sublist_count // 3

def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = current_value

my_l = []
for i in range(501):
    my_l.append(random.randrange(0, 1000))
my_start = time.time()
shell_sort(my_l)
my_end = time.time()
print(my_l)
print('time needed: ', my_end - my_start)