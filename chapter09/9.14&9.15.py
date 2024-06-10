import random  
import string  
    
numbers = list(range(1, 11))   
letters = random.choices(string.ascii_uppercase, k=5)  
combined_list = numbers + letters

winning_combination = random.sample(combined_list, 4) 
   
try_count = 0  

while True:  
    my_ticket = random.sample(combined_list, 4)  
      
    if my_ticket == winning_combination:  
        break  
      
    try_count += 1  
  
print(f"经过 {try_count} 次尝试，终于中了大奖！")