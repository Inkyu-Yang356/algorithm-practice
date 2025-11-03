"""
The Smallest Number in an Array

Input
17, 92, 18, 33, 58, 7, 33, 42

Output
7
"""

def find_min(arr):
    min_num = arr[0]
    for i in range(1, len(arr)):
        if min_num >= arr[i]:
            min_num = arr[i]
    return min_num

arr = list(map(int, input().split()))  # 리스트에 들어갈 정수 입력
print(find_min(arr))