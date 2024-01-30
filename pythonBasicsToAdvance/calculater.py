def add(a ,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def division(a,b):
    return a/b

def modules(a,b):
    return a%b

# print("thanks for using this calculter that is created by nasa scientest")


flag = True
str = """what operation you want to do 
         1: add,
         2:subtract , 
         3: multiply ,
         4:division: and 
         5: modules :"""
while flag:
    operations = int(input(str))
    x = int(input("enter first number: "))
    y = int(input("enter second number: "))

    if operations == 1:
        print(add(x,y))

    elif operations == 2:
        print(subtract(x,y))

    elif operations == 3:
        print(multiply(x,y))

    elif operations == 4:
        print(division(x,y))
    elif operations == 5:
        print(modules(x,y))
    else:
        print("incorrect operation type")

    flag = input("do you want to do more calculation: ")
    if(flag[0].upper() == "N"):
        flag = False