active = True  
while active:  
    topping = input("请输入比萨配料（或输入 'quit' 结束）: ")  
    if topping.lower() == 'quit':  
        active = False  
    else:  
        print(f"比萨中添加的配料: {topping}")