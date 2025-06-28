#Write a program that generates a set of prime numbers and another set of odd 
# numbers. Demonstrate the result of union, intersection, difference, and 
# # symmetric difference operations on these sets.

s1=set()
s2=set()
for i in range(1,101):
    if i%2!=0:
        s1.add(i)
for n in range(1,101):
    for j in range(2,n):
        if n%j!=0:
            s2.add(n)
print("odd number set: ",s1)
print("prime number set: ",s2)
print("Union",s1.union(s2))
print("Intersection",s1.intersection(s2))
print("Difference",s1.difference(s2))
print("Symmetricdifference",s1.symmetric_difference(s2))
