import numpy as np 
data=np.random.randint(50,size=6)
print(data)

#linear search it tike laaarge time to give result
def tyu(arr,targ):
    for ar in arr:
        if ar == targ:
            print('true')
        else:
            print('target is not here')
tyu(data,3)
