human1 = {'first_name':'y', 'last_name':'w', 'age':21, 'city':'Wuhan'}
human2 = {'first_name':'a', 'last_name':'b', 'age':21, 'city':'Wuhan'}
human3 = {'first_name':'c', 'last_name':'d', 'age':21, 'city':'Wuhan'}
list = [human1, human2, human3]
for i in list:
    print(f'{i["first_name"]} {i["last_name"]}')