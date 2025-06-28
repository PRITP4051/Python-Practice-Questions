#wap to convert decimal number to binary

n=int(input("enter the decimal number:"))
s=""
while n>0:
    r=n%2
    s=str(r)+s
    n=n//2
print("binary of given decimal number is:",s)

#wap to convert binary number to decimal
binary = input("Enter a binary number: ")
decimal = 0
power = 0

# Start from the last digit and go to the first
for digit in reversed(binary):
    if digit == '1':
        decimal += 2 ** power
    power += 1

print("Decimal value:", decimal)
