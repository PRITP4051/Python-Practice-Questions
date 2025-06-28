# f=open("demo1.txt","r")
# # data=f.read()
# #data=f.read(5)     #to read only first 5 letters
# line1=f.readline()
# print(line1)
# # print(data)
# # print(type(data))
# f.close()


# f=open("demo1.txt","w")              #delete all data and write a new data
# f.write("i learn dsa from striver")
# f.close()

# f=open("demo1.txt","a")               #append the data behind old data
# f.write("\nstiver is a good youtuber.")
# f.close()


# f=open("demo1.txt","r+")      #overwrite the data at starting
# f.write("abx")                #read+overwrite and pointer=starting
# print(f.read())               #no truncate
# f.close

# f=open("demo1.txt","w+")
# print(f.read())                   #first delete data then we can write data and read data
# f.write("abx")            ##read+overwrite and pointer=starting,truncate
# f.close


# f=open("demo1.txt","r+")      #read data and append data at the end
# print(f.read())
# f.write("prit")                #read+append ,pointer=end,no truncate
# f.close

# with open("demo1.txt","r") as f:
#     print(f.read())
# with open("demo1.txt","w") as f:
#     f.write("new data")

# import os        #to delete any file
# os.remove("sample.txt")


#q-1
#create a new file "practice.txt" using python.add following data in it
#Hi everyone
#we are learning File I/O
#using Python
#I like programming in Python

# with open("practice.txt","w") as f:
#     f.write("#Hi everyone\nwe are learning File I/O\nusing Python\nI like programming in Python")

#q*2
#wap to replece occurence of Python in upper file with Java

# with open("practice.txt","r") as f:
#     data=f.read()
#     print(data)
# new_data=data.replace("Python","Java")
# print(new_data)

# with open("practice.txt","w") as f:
#     f.write(new_data)


#q-3
#search if word "learning" exists in the file or not
# def check_for_word():
#     word="learning"
#     with open("practice.txt","r") as f:
#         data=f.read()
#         if (data.find(word)) !=0:
#             print("found")
#         else:
#             print("Not found")
# check_for_word()


#q-4 
#search in which line word leaning exists
# def check_for_line(word):
#     data=True
#     lineno=1
#     with open("practice.txt","r") as f:
#         while True:
#             data=f.readline()
#             if (word in data):
#                 print(lineno)
#             lineno+=1
#     return -1
# print(check_for_line("learning"))

#q-5
#if file contaiing numbers saperated by comma in file so return count of even
#numbers in that file
def evens():
    count=0
    with open("practice.txt","r") as f:
        data=f.read()
        num=data.split(",")
        for value in num:
            if(int(value)%2==0):
                count+=1
    print(count)
evens()

    