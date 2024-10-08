def linear_search(arr, target):
    
    for index in range(len(arr)):
         
        if arr[index] == target:
            return index  
    return -1 

numbers = [10, 23, 45, 67, 89] 
target = 45 
result = linear_search(numbers, target)  

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the array.")
