#linear search
def linsearch(n, arr):
    for i in range(len(arr)):
        if arr[i] == n:
            print(i)
    return
k=int(input())
print("enter K :",k)
arr=[]
for m in range(k):
    inp=int(input())
    arr.append(inp)
print("enter n:")
n=int(input())
linsearch(n,arr)

#binary search

def binarySearch(arr, low, high, x):

    while low <= high:

        mid = low + (high - low) // 2

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        else:
            high = mid - 1

    # If we reach here, then the element
    # was not present
    return -1


    arr = [2, 3, 4, 10, 40]
    x = 10

    # Function call
    result = binarySearch(arr, 0, len(arr)-1, x)
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")

