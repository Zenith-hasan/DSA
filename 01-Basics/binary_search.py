

#?  Binary Search

# This below code is the implementaion of binary Search Using Recursive method


def binarySearch(arr,low,high,x):
    
    if high >= low:
        mid = (low + high) // 2
        if arr[mid] == x :
            return mid
        elif arr[mid] > x :
            return binarySearch(arr,low,mid-1,x)
        elif arr[mid] < x :
            return binarySearch(arr,mid + 1,high,x)
    else:
        return -1
    
    
    
arr = [2,3,8,9,23,67,78]
x = 23
result = binarySearch(arr,0,len(arr) - 1, x)
if result != -1 :
    print(f"Element present at index -> {result}")
else :
    print("Element not present in the list")