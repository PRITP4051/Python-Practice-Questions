
#star patterns

#q-1

# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * * 

# n=5
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#     print()

#method 2
def print_square_stars(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()

# Example usage:
print_square_stars(3)
print_square_stars(5)
#q-2

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 

# n=5
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

#q-3

# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

# n=5
# for i in range(n):
#     for j in range(i,n):
#         print("*",end=" ")
#     print()

#q-4

# * * * * *
#   * * * *
#     * * *
#       * *
#         *

# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):      #two triangle
#         print("*",end=" ")    #incrising space triangle + decreaseing star triangle
#     print()

#q-5

#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * *

# n=5
# for i in range(n):

#     for j in range(i,n):      #two triangle
#         print(" ",end=" ") 
#     for j in range(i+1):
#         print("*",end=" ")   #incrising star triangle + decreaseing space triangle
#     print()

#q-6

#         * 
#       * * * 
#     * * * * * 
#   * * * * * * * 
# * * * * * * * * * 

# n=5
# for i in range(n):

#     for j in range(i,n):      #three triangle
#         print(" ",end=" ") 
#     for j in range(i):        #one star triangle will be small by 1
#         print("*",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")   # decreaseing space triangle + incrising star triangle+
#     print()                  # decreaseing star triangle

#q-7

# * * * * * * * * * 
#   * * * * * * * 
#     * * * * * 
#       * * * 
#         * 

# n=5
# for i in range(n):

#     for j in range(i+1):      #three triangle
#         print(" ",end=" ") 
#     for j in range(i,n-1):        #one star triangle will be small by 1
#         print("*",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")   # incrising space triangle + decreaseing star triangle+
#     print()                  # decreaseing star triangle

#q-8

#         * 
#       * * * 
#     * * * * * 
#   * * * * * * * 
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

# n=5
# for i in range(n-1):

#     for j in range(i,n):      #three triangle
#         print(" ",end=" ") 
#     for j in range(i):        #one star triangle will be small by 1
#         print("*",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")   # decreaseing space triangle + incrising star triangle+
#     print()                  # decreaseing star triangle

# for i in range(n):

#     for j in range(i+1):      #three triangle
#         print(" ",end=" ") 
#     for j in range(i,n-1):        #one star triangle will be small by 1
#         print("*",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")   # incrising space triangle + decreaseing star triangle+
#     print()                  # decreaseing star triangle

