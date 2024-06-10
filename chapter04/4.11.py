pizzas = ['a', 'b', 'c']
friend_pizzas = pizzas[:]
pizzas.append('d')
friend_pizzas.append('e')
print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza)
print('My friend\'s favorite pizzas are:')
for pizza in friend_pizzas:
    print(pizza)