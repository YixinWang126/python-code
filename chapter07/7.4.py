while True:  
    topping = input("请输入比萨配料（或输入 'quit' 结束）: ")  
    if topping.lower() == 'quit':  
        break  
    print(f"比萨中添加的配料: {topping}")