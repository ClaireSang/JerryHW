def cal(operator,*args):
    x1 = 0
    x2 = 0

    for i in args:
        if x1 == 0:
            x1 = i
        else:
            x2 = i

    if(operator == "+"):
        print(x1,"+",x2,"=",(x1+x2))
    elif(operator == "-"):
        print(x1,"-",x2,"=",(x1-x2))
    elif(operator == "*"):
        print(x1,"x",x2,"=",(x1*x2))
    elif(operator == "/"):
        print(x1,"÷",x2,"=",(x1/x2))