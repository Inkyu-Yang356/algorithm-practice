friends_info = {
    'Summer' : ['John', 'Justin', 'Mike'],
    'John' : ['Summer', 'Justin'],
    'Justin' : ['Summer', 'John', 'Mike', 'May'],
    'Mike' : ['Summer', 'Justin'],
    'May' : ['Justin', 'Kim'],
    'Kim' : ['May'],
    'Tom' : ['Jerry'],
    'Jerry' : ['Tom']
}

from collections import deque

def find_friends(g, s):  # g = graph, s = start
    qu = deque([s])
    done = set()
    done.add(s)

    while qu:
        node = qu.popleft()  # pop() from left
        print(node)
        for n in g[node]:  # New nodes
            if n not in done:  # If it has not been to n
                done.add(n)
                qu.append(n)

find_friends(friends_info, 'Summer')