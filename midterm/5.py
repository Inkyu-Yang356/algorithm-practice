""" 
Insertion Sort to a Specific Index

Input
11 5
3 1 4 1 5 9 2 6 5 3 5

Output
1 1 3 4 5 9 2 6 5 3 5
"""

length, specific_idx = map(int, input().split())
arr = list(map(int, input().split()))

# 인덱스 제한
if len(arr) > specific_idx:
    remaining = arr[specific_idx:]
    arr = arr[:specific_idx]
    

def insertion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1  # i는 1, j는 0부터 순차적으로 비교 시작
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1]=key

insertion(arr)
for i in arr + remaining:
    print(i, end=' ')