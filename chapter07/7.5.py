while True:  
    age = int(input("请输入您的年龄（或输入非数字结束）: "))  
    if age < 0:  # 假设非数字或负数输入为结束  
        break  
    if age < 3:  
        print("免费")  
    elif 3 <= age < 12:  
        print("票价为 10 美元")  
    else:  
        print("票价为 15 美元")