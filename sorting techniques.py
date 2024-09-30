# Selection Sort
A = [64, 25, 12, 22, 11]

# Traverse through all array elements
for i in range(len(A)-1):
    
    # Find the minimum element in remaining 
    # unsorted array
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
            
    # Swap the found minimum element with 
    # the first element        
    A[i], A[min_idx] = A[min_idx], A[i]

# Driver code to test above
print ("Sorted array")
for i in range(len(A)):
    print(A[i],end=" ") 
# Optimized Python program for implementation of Bubble Sort


def bubbleSort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]

    bubbleSort(arr)

    print("Sorted array:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")

#merge Sort
def mergesort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
        mergesort(left)
        mergesort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[i]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

arr = [12, 11, 13, 5, 6, 7]
mergesort(arr)
print("Sorted array:", arr)

#quick sort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[-1]  
        left = [x for x in arr[:-1] if x <= pivot]
        right = [x for x in arr[:-1] if x > pivot]
        return quicksort(left) + [pivot] + quicksort(right)

arr = [10, 80, 30, 90, 40, 50, 70]
sorted_arr = quicksort(arr)
print("Sorted array:", sorted_arr)
def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    output = [0] * len(arr)

    # Step 3: Count occurrences
    for num in arr:
        count[num] += 1

    # Step 4: Cumulative count
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Step 5: Build output array
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    # Step 6: Copy output back to original array
    for i in range(len(arr)):
        arr[i] = output[i]

# Example usage
arr = [4, 2, 2, 8, 3, 3, 1]
counting_sort(arr)
print("Sorted array:", arr)
