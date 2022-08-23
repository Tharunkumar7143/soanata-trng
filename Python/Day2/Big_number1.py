def Big(a,b,c):
    if (a > b) and (a > c):
        return "a is big", a
    elif (b > a) and (b > c):
        return "b is big", b
    else:
        return "c is big", c
    
result=Big(70,60,143)
print(result)