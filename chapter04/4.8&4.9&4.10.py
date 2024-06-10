list = [i**3 for i in range(1,11)]
for i in list:
    print(i)

print(f'The first three items in the list are:{list[0:3]}')
print(f'Three items from the middle of the list are:{list[1:4]}')
print(f'The last three items in the list are:{list[-3:]}')