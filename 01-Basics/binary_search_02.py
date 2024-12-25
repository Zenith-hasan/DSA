
#? Binary Search

# This is am implementaion of the binary search using iterative approach

def binarySearch(arr,x):
    low = 0
    high = len(arr)-1
    mid = 0
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > x :
            high = mid -1
        elif arr[mid] < x :
            low = mid + 1
        else:
            return mid
    return -1
arr = [3,5,7,9,33,56,87,99]
x = 7

result = binarySearch(arr,x)

if result != -1 :
    print(f"Element present at index : {result}")
else :
    print("Element not present in the list!")
 