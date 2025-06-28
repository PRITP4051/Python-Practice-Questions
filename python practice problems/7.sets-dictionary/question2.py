#Write a program that creates two sets. One of even number in range 1-10 and 
# the other has all composite numbers in range 1-20. Demonstrate the use of 
# all(), isuperset(), len(), sum(), update(), pop(), remove(), add() and clear() 
# functions on sets.
even = set(range(2, 11, 2))
compo = set()
for num in range(4, 21):
    for i in range(2, int(num/2) + 1):
        if num % i == 0:
            compo.add(num)
            break
print(all(even))
print("Even Numbers:", even)
print("Composite Numbers:", compo)
print(even>=compo)
print(len(even))
print(len(compo))
print(sum(even))
even.update(compo)
print(even)
print(even.pop())
even.remove(10)
print(even)
even.add(10)
print(even)
compo.clear()
print(compo)