#AttributeError

# s={1,2,3,4,5}
# s.append(6)
# print(s)

try:
    s={1,2,3,4,5}
    s.append(6)
    print(s)
except AttributeError:
    print("can not show output.")
    