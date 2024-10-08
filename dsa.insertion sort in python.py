
arr = [64, 34, 25, 12, 22, 11, 9]
for i in range(1, len(arr)):
    cur = arr[i]  
    j = i - 1
    while j >= 0 and cur < arr[j]:
        arr[j + 1] = arr[j]  
        j -= 1
    arr[j + 1] = cur
print("Sorted array:", arr)
