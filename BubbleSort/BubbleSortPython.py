#Python code for bubble sort
def BubbleSort(array):
    #this line sets a variable for how much of the array is unsorted. As elements get sorted at the back, this value decreases.
    unsortedSize = array.size
    #This line sets a boolean value to help check if we have iterated through the array without swapping any values. If this is the case, the array is sorted
    #If python had a do-while loop, we could initalize this variable inside the loop. But since the while loop starts by checking this variable, we initialize it here.
    passvalue = False
    #This begins the iterative portion. It uses a while condition because we can stop if passvalue is every set to true.
    while(passvalue != True):
        passvalue = True #passvalue will change to false only if a swap has been made.
        for i in range (unsortedSize-1): #iterating through the unsorted part of the array
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1],array[i] #swap
                passvalue = False #Set passvalue to false so the while loop repeats
        unsortedSize -= 1 #decrementing unsortedSize since we don't need to check the sorted part of the array

#In other languages, a return statement would be needed not only to end the function, but to be able to retrieve the sorted array in the calling environment
#But in python, changes to variables inside a function update the global variable. If array X is passed to this function, the array that is stored in the calling envrionment
#will be the one the function is manipulating. 
        
#The time complexity for bubble sort is typically O(n^2), since in the worst case it will pass through every value of the array n number of times. 
#However, since we reduce the size of the array that we are checking with each iteration and we also have a method to end the function if no swapping is done,
#it will likely not take n^2 time. 

#Bubble sorting is a stable, in place sorting algorithm This means that the sorting will happen with the array we want to sort (in place),
#and data points with duplicate keys but different values will have the same relative position from before sorting i.e. if we were sorting 
#the windows file system by date and two files had the same date, they would have the same position relative to each other as before (stable).
