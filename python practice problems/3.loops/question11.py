#number patterns
#q-1
#    1
#    2 2
#    3 3 3
#    4 4 4 4
#    5 5 5 5 5

# n=5
# p=1
# for i in range(n):
#     for j in range(i+1):
#         print(p,end=" ")
#     p+=1
#     print()

#q-2
#   5
#   4 4
#   3 3 3
#   2 2 2 2
#   1 1 1 1 1

# n=5
# p=5
# for i in range(n):
#     for j in range(i+1):
#         print(p,end=" ")
#     p-=1
#     print()

#q-3
#   0
#   2 2
#   4 4 4
#   6 6 6 6
#   8 8 8 8 8

# n=5
# p=0
# for i in range(n):
#     for j in range(i+1):
#         print(p,end=" ")
#     p+=2
#     print()

#q-4
#   1                               #imp
#   2 2
#   1 1 1
#   2 2 2 2
#   1 1 1 1 1

# n=5
# for i in range(n):
#     for j in range(i+1):
#         if i%2==0:
#             print("1",end=" ")
#         else:
#             print("2",end=" ")
#     print()

#q-5
#            1
#          2 2 2
#        3 3 3 3 3
#      4 4 4 4 4 4 4
#    5 5 5 5 5 5 5 5 5
#      6 6 6 6 6 6 6
#        7 7 7 7 7
#          8 8 8
#            9

# n=5
# p=1
# for i in range(n-1):

#     for j in range(i,n):      #three triangle
#         print(" ",end=" ") 
#     for j in range(i):        
#         print(p,end=" ")
#     for j in range(i+1):
#         print(p,end=" ")   
#     print()                  
#     p+=1
# for i in range(n):

#     for j in range(i+1):      
#         print(" ",end=" ") 
#     for j in range(i,n-1):       
#         print(p,end=" ")
#     for j in range(i,n):
#         print(p,end=" ")   
#     print()   
#     p+=1               

# q-6
    #          1
    #        2 2 2
    #      3 3 3 3 3
    #    4 4 4 4 4 4 4
    #  5 5 5 5 5 5 5 5 5
    #    4 4 4 4 4 4 4
    #      3 3 3 3 3
    #        2 2 2
    #          1
# n=5
# p=1
# for i in range(n-1):

#     for j in range(i,n):      #three triangle
#         print(" ",end=" ") 
#     for j in range(i):        
#         print(p,end=" ")
#     for j in range(i+1):
#         print(p,end=" ")   
#     print()                  
#     p+=1
# for i in range(n):

#     for j in range(i+1):      
#         print(" ",end=" ") 
#     for j in range(i,n-1):       
#         print(p,end=" ")
#     for j in range(i,n):
#         print(p,end=" ")   
#     print()   
#     p-=1               
#q-7                                #imp
#    1                              #different row values
#    1 2
#    1 2 3
#    1 2 3 4
#    1 2 3 4 5

# n=5
# for i in range(n):
#     p=1
#     for j in range(i+1):
#         print(p,end=" ")
#         p+=1
#     print()

#q-8
#   1 2 3 4 5
#   1 2 3 4
#   1 2 3
#   1 2
#   1

# n=5
# for i in range(n):
#     p=5
#     for j in range(i,n):
#         print(p,end=" ")
#         p-=1
#     print()

#q-9

#            1
#          1 2 3
#        1 2 3 4 5
#      1 2 3 4 5 6 7
#    1 2 3 4 5 6 7 8 9

# n=5
# for i in range(n):
#     p=1
#     for j in range(i,n):     
#         print(" ",end=" ") 
#     for j in range(i):        
#         print(p,end=" ")
#         p+=1
#     for j in range(i+1):
#         print(p,end=" ")  
#         p+=1  
#     print() 

#q-10
#   5
#   5 4
#   5 4 3                         #staring same ending different
#   5 4 3 2
#   5 4 3 2 1

# n=5
# for i in range(n):
#     p=5
#     for j in range(i+1):
#         print(p,end=" ")
#         p-=1
#     print()

#q-11
#   5 4 3 2 1
#     4 3 2 1
#       3 2 1        #staring different ending same
#         2 1
#           1

# n=5
# k=5                                  #most ImP
# for i in range(n):
#     p=k
#     for i in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print(p,end=" ")
#         p-=1
#     k-=1
#     print()

#q-12
    #         1
    #       1 2 1
    #     1 2 3 2 1
    #   1 2 3 4 3 2 1
    # 1 2 3 4 5 4 3 2 1
# n=5
# for i in range(n):
#     p=1
#     for j in range(i,n):     
#         print(" ",end=" ") 
#     for j in range(i):        
#         print(p,end=" ")
#         p+=1
#     for j in range(i+1):
#         print(p,end=" ")  
#         p-=1  
#     print() 

#q-13
#   1
#   2 3
#   4 5 6
#   7 8 9 10

# n = 4
# p=1
# for i in range(n):
#     for j in range(i+1): 
#         print(p, end=' ')
#         p+=1
#     print()

