#WAP that prints histogram of frequencies of characters occurring in a massage
msg ="Hello All,My name is Prit"
msg = msg.lower()
Dict =dict()
for char in msg:
    if char not in Dict:
        Dict[char] =1
    else:
        Dict[char] = Dict[char] +1
print(Dict)
for key,val in Dict.items():
    print(key,'\t','*'* val)