current_users = ['admin', 'Panimonz', 'Cristiano', 'Mori', 'Vaundy']
users = []
for i in current_users:
    users.append(i.lower())
print(users)
new_users = ['Panimonz', 'Cristiano', 'x', 'y', 'z']
for i in new_users:
    if i.lower() in users:
        print('需要输入别的用户名')
    else:
        print('This name hasn\'t been used.')
