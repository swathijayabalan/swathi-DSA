def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) //2 
        
        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            low = mid + 1 
        else:
            high = mid - 1 
    return -1 

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
result = binary_search(arr, target)
print("Index of target:", result)
