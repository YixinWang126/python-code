number_of_people = int(input("请问有多少人用餐？ "))  
  
# 检查人数是否超过8人  
if number_of_people > 8:  
    print("对不起，没有空桌。")  
else:  
    print("有空桌，欢迎用餐。")