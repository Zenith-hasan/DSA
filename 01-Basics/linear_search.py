
#? Linear Search 


# linear search using the iterative approach

def linearSearch(arr,target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1


arr = [45,2,67,1,8,90]
x = 1

result = linearSearch(arr,x)

if result != -1 :
    print(f"Element found at the index : {result}")
else:
    print("Element not present in the array!")