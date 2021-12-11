#Code to make unsorted Array
import numpy as np

def MakeArray():
    Arr = np.array([np.random.randint(100, size=50)])
    return Arr
print(MakeArray())
