
#WAP to demonstrate the use of various in-built functions in dictionary.

Dict = {'Roll_No':230136,'Name':'Prit','Course':'BTech'}
print("LEN : ",len(Dict))
print("STRING : ",str(Dict))
Dict.clear()
print("CLEAR : ", Dict)
Subject = ['PP','Maths','DS','CP']
Marks =dict.fromkeys(Subject,-1)
print("FROMKEYS : ", Marks)
Dict = {'Roll_No':230148,'Name':'Dirgh','Course':'BTech'}
print("GET KEYS : ", Dict.get('Name'))
print("ITEMS : ", Dict.items())
print("KEYS : ", Dict.keys())
Dic = {'Marks':95,'Grade':'A'}
Dict.update(Dic)
print("UPDATE : ", Dict)
print("VALUES : ", Dict.values())