def bubbleSort(arr):
	n = len(arr)
	swapped = False
	for i in range(n-1):
		for j in range(0, n-i-1):
			if arr[j] > arr[j + 1]:
				swapped = True
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
		
		if not swapped:      
			return arr

arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
	print("% d" % arr[i], end=" ",)

print('\n')

import numpy as np

def doublle(arry):
    n=len(arry)
    swap=False
    for i in range(n-1):
        #n-1 for make it start on 0 not 1, 0 1 2 3 4...
        for y in range(0,n-i-1):
            if arry[y] > arry[y+1]:
                sawp=True
                arry[y],arry[y+1]=arry[y+1],arry[y]
        if not swap:
            print(arry)
arry=np.random.randint(100,size=8)
doublle(arry)




