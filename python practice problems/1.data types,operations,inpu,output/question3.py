#wap to interchange the values of given two variables

a=10
b=15
print("before interchange values a=",a,"b=",b)
temp=a
a=b
b=temp  # take third variable temp
print("after interchange values a=",a,"b=",b)


# swap using assinment operators

a=10
b=15
print("before interchange values a=",a,"b=",b)
a,b=b,a
print("after interchange values a=",a,"b=",b)