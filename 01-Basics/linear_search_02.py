
#? Linear Search 

# This is a linear search using the recursive appraoch


def linearSearchRecursive(arr,target, index = 0 ):
    
    if index == len(arr):
        return -1
    if arr[index] == target:
        return index
    return linearSearchRecursive(arr,target,index + 1)


arr = [3,65,12,45,8,90,56,78,90,0,2]
target = 90

result = linearSearchRecursive(arr,target)

if result != -1 :
    print(f"Element is present at index: {result}")
else :
    print("Element not present in the list!")
    
