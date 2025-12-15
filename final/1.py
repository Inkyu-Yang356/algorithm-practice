def binary_search(arr, x):  # Find target value in the input
    start=0
    end=len(arr)-1
    
    while end >= start:
        mid = (start + end) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:  # adjust index
            start = mid+1
        else:
            end = mid-1
    return -1

#a = [1,4,9,16,25,36,49,64,81]
#x = 36

a = list(map(int, input().split()))  # Sorted Array Input
x = int(input())  # Target Index
y = binary_search(a, x)
print(y)