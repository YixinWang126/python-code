import random  
  
class Die:  
    def __init__(self, sides=6):  
        self.sides = sides    
    def roll_die(self):  
        return random.randint(1, self.sides)  
  
die_6 = Die(6)  
for _ in range(10):  
    print(die_6.roll_die())  
print()  
  
die_10 = Die(10)  
for _ in range(10):  
    print(die_10.roll_die())  
print()  

die_20 = Die(20)  
for _ in range(10):  
    print(die_20.roll_die())  
print() 