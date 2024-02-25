def insertionSort(arr,n):
    print(arr)
    
    for i in range(1, n):
        key = arr[i]
        print(key)
        kbal = i-1
        while kbal >= 0 and key < arr[kbal]:
                arr[kbal + 1] = arr[kbal]
                kbal -= 1
        arr[kbal + 1] = key
        print(arr)

import numpy as np
n=6
arr=np.random.randint(45,size=n) 

insertionSort(arr,n)





import numpy as np

def inset(arr,n):
    for i in range(1,n):
        fir=arr[i] #1
        bfr=i-1  #0
        while bfr >= 0 and fir < arr[bfr]:
            arr[bfr+1]=arr[bfr]
            bfr-=1
        arr[bfr+1]=fir
        print(arr)
n=12
arr= np.random.randint(100,size=n)
inset(arr,n)




