#Implement the bubble sort using simultaneous assignment
import random, time
def bubble_sort(a_list):
    for pass_num in range(len(a_list) - 1, 0, -1):
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp


my_list = []
for _ in range(10):
    my_list.append(random.randrange(0, 100))
    bubble_sort(my_list)
end = time.time()
print(my_list)
