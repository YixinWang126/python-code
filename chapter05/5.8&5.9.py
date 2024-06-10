#users = ['admin', 'Panimonz', 'Cristiano', 'Mori', 'Vaundy']
users = []
if not users:
    print('We need to find some users!')
for usr in users:
    if usr == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print(f'Hello {usr}, thank you for logging in again.')
