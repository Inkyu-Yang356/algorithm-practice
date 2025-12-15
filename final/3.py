def print_all_friends():
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

    print(friends_info)

print_all_friends()