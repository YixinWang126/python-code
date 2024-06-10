sandwich_orders = ["tuna", "ham", "cheese", "turkey", "roast beef", 'pastrami', 'pastrami', 'pastrami']  
s = sandwich_orders[:]
finished_sandwiches = []  
   
for sandwich in s:  
    print(f"I made your {sandwich} sandwich.")  
    sandwich_orders.remove(sandwich)
    finished_sandwiches.append(sandwich)  
 
print("All sandwiches have been made:")  
for sandwich in finished_sandwiches:  
    print(sandwich)

print(sandwich_orders)