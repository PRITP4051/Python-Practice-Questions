#WAP to access values stored in a dict, add a new item in the dict, modify an 
# item in the dict, remove an element from dict. 

dict={"Name":"Prit Patel","roll no":"230136","marks":96}
print(dict["Name"])
dict["city"]="Ahemdabad"
print(dict)
dict["marks"]=85
print(dict)
del dict["roll no"]
print(dict)