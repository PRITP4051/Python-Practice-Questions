#charector patterns
#q-1
# A 
# A A 
# A A A 
# A A A A 
# A A A A A

# n=5
# for i in range(n):
#    for j in range(i+1):
#       print('A', end=' ')
#    print()

#q-2
# A                                 
# B B 
# C C C 
# D D D D 
# E E E E E


# n = 5
# p=65
# for i in range(n): 
#    for j in range(i+1): 
#       print(chr(p), end=' ')
#    p+=1
#    print()

#q-3
# A 
# C C 
# E E E 
# G G G G 
# I I I I I

# n = 5
# p=65
# for i in range(n): 
#    for j in range(i+1): 
#       print(chr(p), end=' ')
#    p+=2
#    print()

#Q-4
# A 
# B B 
# A A A 
# B B B B 
# A A A A A

# n = 5
# for i in range(n): 
#     for j in range(i+1):
#       if(i%2==0):
#          print("A", end=' ')
#       else:
#          print("B", end=' ')
#     print()

#q-5
# Z Z Z Z Z 
#   0 0 0 0 
#     Z Z Z 
#       0 0 
#         Z

# n = 5 
# for i in range(n): 
#    for j in range(i): 
#       print(' ', end=' ') 
#    for j in range(i, n):
#       if(i%2==0):
#          print("Z", end=' ')
#       else:
#          print("0", end=' ')
#    print()

#q-6
#           A 
#         B B B 
#       C C C C C 
#     D D D D D D D 
#   E E E E E E E E E 
#     F F F F F F F
#       G G G G G 
#         H H H
#           I

# n=5
# p=65
# for i in range (n-1):
#   for j in range (i,n):
#      print (' ', end = ' ')
#   for j in range (i):
#      print (chr(p), end = ' ') 
#   for j in range (i+1):
#      print (chr(p), end = ' ') 
#   p+=1
#   print() 
# for i in range (n):
#    for j in range (i+1):
#       print (' ', end = ' ')
#    for j in range (i,n-1):
#       print (chr(p), end = ' ') 
#    for j in range (i,n):
#       print (chr(p), end = ' ') 
#    p+=1
#    print()

#q-7
#           A 
#         B B B 
#       C C C C C 
#     D D D D D D D 
#   E E E E E E E E E 
#     D D D D D D D 
#       C C C C C 
#         B B B 
#           A 

# n=5
# p=65
# for i in range (n-1):
#   for j in range (i,n):
#      print (' ', end = ' ')
#   for j in range (i):
#      print (chr(p), end = ' ') 
#   for j in range (i+1):
#      print (chr(p), end = ' ') 
#   p+=1
#   print() 
# for i in range (n):
#    for j in range (i+1):
#       print (' ', end = ' ')
#    for j in range (i,n-1):
#       print (chr(p), end = ' ') 
#    for j in range (i,n):
#       print (chr(p), end = ' ') 
#    p-=1
#    print()

#q-8
# A 
# A B 
# A B C 
# A B C D 
# A B C D E 

# n=5
# for i in range(n):
#    p=65
#    for j in range(i+1):
#       print(chr(p), end=' ')
#       p+=1
#    print()

#q-9
# A B C D E 
#   A B C D 
#     A B C 
#       A B 
#         A

# n = 5 
# for i in range(n):
#    p=65 
#    for j in range(i): 
#       print(' ', end=' ') 
#    for j in range(i, n):
#         print(chr(p), end=' ')
#         p+=1
#    print()

#q-10
#           A  
#         A B C  
#       A B C D E  
#     A B C D E F G  
#   A B C D E F G H I 

# n=5
# for i in range (n):
#   p=65
#   for j in range (i,n):
#      print (' ', end = ' ')
#   for j in range (i):
#      print (chr(p), end = ' ') 
#      p+=1
#   for j in range (i+1):
#      print (chr(p), end = ' ') 
#      p+=1
#   print()

#q-11
# E 
# E D              #same staring different ending
# E D C 
# E D C B 
# E D C B A 

# n = 5
# for i in range(n): 
#    p=69
#    for j in range(i+1): 
#       print(chr(p), end=' ')
#       p-=1
#    print()

#q-12        #most imp
# E D C B A 
#   D C B A 
#     C B A 
#       B A 
#         A 

# n=5
# k=69                                  #most ImP
# for i in range(n):
#     p=k
#     for i in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print(chr(p),end=" ")
#         p-=1
#     k-=1
#     print()

#q-13
#           A 
#         A B A 
#       A B C B A 
#     A B C D C B A 
#   A B C D E D C B A 

# n = 5 
# for i in range(n): 
#    p=65
#    for j in range(i, n): 
#       print(' ', end=' ') 
#    for j in range(i):
#       print(chr(p), end=' ')
#       p+=1
#    for j in range(i+1):
#       print(chr(p), end=' ')
#       p-=1
#    print()

#q-14
# C 
# O O 
# D D D 
# E E E E 
# R R R R R

# s = "CODER" 
# n = len(s)
# p = 0
# for i in range(n): 
#    for j in range(i+1): 
#       print(s[p], end = ' ')
#    p+=1
#    print()

#q-15
# R 
# E E 
# D D D 
# O O O O 
# C C C C C

# s = "CODER" 
# n= len(s)
# p= n-1
# for i in range(n): 
#    for j in range(i+1): 
#       print(s[p], end=' ')
#    p-=1
#    print()

#q-16
# C 
# C O 
# C O D 
# C O D E 
# C O D E R

# s = "CODER" 
# n= len(s)
# for i in range(n):
#    p=0
#    for j in range(i+1): 
#       print(s[p], end=' ')
#       p+=1
#    print()

#q-17
# R 
# R E 
# R E D 
# R E D O 
# R E D O C

# s = "CODER" 
# n= len(s)
# for i in range(n):
#    p=n-1
#    for j in range(i+1): 
#       print(s[p], end=' ')
#       p-=1
#    print()

#q-18      most imp
# R E D O C 
#   E D O C 
#     D O C 
#       O C               #diff start same end 
#         C

# s = "CODER" 
# n = len(s)
# k = n-1
# for i in range(n): 
#    p=k
#    for j in range(i): 
#       print(' ', end=' ') 
#    for j in range(i, n):
#       print(s[p], end=' ')
#       p-=1
#    print()
#    k-=1