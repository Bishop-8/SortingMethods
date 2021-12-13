#Python code for bubble sort
def BubbleSort(array):
    unsortedSize = array.size
    passvalue = False
    while(passvalue != True):
        passvalue = True
        for i in range (unsortedSize-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1],array[i]
                passvalue = False
        unsortedSize -= 1
    return array

  #The time complexity for bubble sort is typically O(n^2), since in the worst case it will pass through every value of the array n number of times. 
#However, since we reduce the size of the array that we are checking with each iteration and we also have a method to end the function if no swapping is done,
#it will likely not take n^2 time. 

#Bubble sorting is a stable, in place sorting algorithm This means that the sorting will happen with the array we want to sort (in place),
#and data points with duplicate keys but different values will have the same relative position from before sorting i.e. if we were sorting 
#the windows file system by date and two files had the same date, they would have the same position relative to each other as before (stable).
