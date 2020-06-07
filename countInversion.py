#In this program Count Inversion is implemented using Merge Sort.

#Fuction to use Inversion Count.

def mergeSort(arr, n):
    #temp array to store sorted array.
    tempArray = [0] * n
    return _mergeSort(arr, tempArray, 0, n-1)

#Following function will you mergeSort to Count Inversions.


def _mergeSort(arr, tempArray, left,right):

    #Variable invCount is used to store number of inversion counts in each recursive call.

    invCount = 0


    #The Recursive function will work if and only if we have more than one elements into the array.

    if left < right:

        #calculating mid using floor function.
        mid = (left + right)//2

        #Calculating number of inversions in left subarray.

        invCount += _mergeSort(arr, tempArray, left, mid)

        #Calculating number of inversions in right subarray.

        invCount += _mergeSort(arr, tempArray, mid + 1, right)

        #Merging two sub arrays in a sorted array.

        invCount += merge(arr, tempArray, left, mid, right)
    return invCount

#Following function will merhge to sub arrays in a single sorted sub array. 

def merge(arr, tempArray, left, mid, right):
    i = left #Starting index of a left Subarray
    j = mid + 1 #Starting index of a right subarray
    k = left #Starting index of to be sorted Subarray

    invCount = 0

    #Conditions to check that i and j are not exceeding the subarray limit.

    while i <= mid and j <= right:

        #If arr[i] <= arr[j] the there will be no inversions.

        if arr[i] <= arr[j]:
            tempArray[k] = arr[i]
            k += 1
            j += 1
        else:
            tempArray[k] = arr[j]
            invCount += (mid - i + 1)
            k += 1 
            j += 1
    
    #Copy remaining elements of left subarray into temp array

    while i <= mid:
        tempArray[k] = arr[i]
        k += 1
        i += 1
    
    #Copy remaining elements of right subarray into temp array

    while j <= right:
        tempArray = arr[j]
        k += 1
        j += 1

    #Copy the sorted subarray into Original array
    for loop_var in range(left , right + 1):
        arr[loop_var] = tempArray[loop_var]

    return invCount

#Driver Code

arr = [8,4,2,1]
n = len(arr)

result  = mergeSort(arr, n)

print("Number of Inversions: ", result)



