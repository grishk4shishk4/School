import random

num_list = []
for i in range(15):
    num_list.append(random.randint(1, 15))

counter = 0

def bogoSort(arr, counter):
    while (sorted(arr) != arr):
        random.shuffle(arr)
        counter += 1
    return arr, counter
print(bogoSort(num_list, counter))