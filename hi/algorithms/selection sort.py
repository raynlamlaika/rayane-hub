import numpy as np
size=int(input('chose the size of array :  '))
array= np.random.randint(100,size=size)
print(array)
def selectionSort(array, size):
    for i in range(size):
        min_i = i
        for j in range(i + 1, size):
            # select the minimum element in every iteration
            if array[j] < array[min_i]:
                min_i = j
        (array[i], array[min_i]) = (array[min_i], array[i])
        print(i,min_i)
        print(array)
        
selectionSort(array,size)
