 dog = {"type": "Dog", "owner": "John"}  
cat = {"type": "Cat", "owner": "Jane"}  
hamster = {"type": "Hamster", "owner": "Alice"}  
  
pets = [dog, cat, hamster]  
  
for pet in pets:  
    print(f"Pet type: {pet['type']}, Owner: {pet['owner']}")