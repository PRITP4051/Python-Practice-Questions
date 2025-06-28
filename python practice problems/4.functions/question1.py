#Write functions to find addition, subtraction, multiplication, and division of a 
# two given numbers. 
def add(a,b):
    print(a,"+",b,"=",a+b)
    return a+b

def diff(a,b):
    s=a-b
    print(a,"-",b,"=",s)
    return s

def mul(a,b):
    s=a*b
    print(a,"*",b,"=",s)
    return s

def div(a,b):
    s=a/b
    print(a,"/",b,"=",s)
    return s

add(20,10)
diff(20,10)
mul(20,10)
div(20,10)

