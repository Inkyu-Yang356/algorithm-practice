"""
Palindrome and Recursion Count

Input
5
AAA
ABBA
ABABA
ABCA
PALINDROME

Output
1 2
1 3
1 3
0 2
0 1
"""

n = int(input())
s = []

def recursion(s, l, r, count=0):
    count += 1
    if l >= r: return 1, count
    elif s[l] != s[r]: return 0, count
    else: return recursion(s, l+1, r-1, count)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, count)

count = 0
for i in range(n):
    s.append(input())
    result, cnt = isPalindrome(s[i])
    print(result, cnt)
    