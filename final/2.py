def is_palindrome(s):
    qu = []
    st = []
    
    for l in s:  # each letter in string
        if l.isalpha():  # if l = alphabet, return True
            qu.append(l.lower())  # lower case for comparison
            st.append(l.lower())

    while qu and st:
        if qu.pop(0) != st.pop():  # Queue(First in First out), Stack(First in Last out)
            return False
        
    return True

#s = 'Wow'

s = input()
result = is_palindrome(s)
print(result)