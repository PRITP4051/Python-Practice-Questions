#open a file using two mwthods

#method 1
# file1=open("demo.txt","w")
# file1.write("hello world")
# file1.close()

#method 2
with open("demo.txt","r") as f:
    print(f.read())

