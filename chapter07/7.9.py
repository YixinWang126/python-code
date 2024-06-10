sandwich_orders = ["tuna", "ham", "cheese", "turkey", "roast beef", 'pastrami', 'pastrami', 'pastrami']  
print('Pastrami is sold out!')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)