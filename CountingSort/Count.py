
import numpy as np

def MakeArray():
    Arr = np.random.randint(100, size=50)
    return Arr
max = 50
Arr = MakeArray()
for i in np.nditer(Arr):
    print(i, end=" ")
for i in np.nditer(Arr):
    if(i>max):
        max = i
print('max= ',max)
CountArray = np.zeros([max+1], dtype=int)
for i in np.nditer(Arr):
    CountArray[i] = CountArray[i] + 1
for i in np.nditer(CountArray):
    print(i, end=" ")
print('\n')
for i in range(1,max+1):
    CountArray[i] = CountArray[i] + CountArray[i-1]
for i in np.nditer(CountArray):
    print(i, end=" ")
print('\n')
for i in range(0,max+1):
    if(CountArray[0] > 0):
        Arr[0] = 0
    if(i > 0):
        while(CountArray[i]>CountArray[i]-1):
            Arr[CountArray[i-1]] = i
            i++
            DEAL WITH DUPLICATES
for i in np.nditer(Arr):
    print(i, end=" ")
    
