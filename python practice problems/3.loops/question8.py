# # WAP that asks the user to enter a password. If the user enters the right password, 
# the program should tell the user that ‘You are logged in to the system’. Otherwise, 
# the program should tell to reenter the password. The user should only get five tries 
# to enter the password, after which the program should tell the user that ‘Number of 
# attempts exceeds, you cannot log in to the system’. 

password="prit@2005"
n=input("enter your password:")
i=0
while i<5:
    
    if n==password:
        print("You are logged in to the system")
        break
    else:
        i+=1
        print(input("re enter the password:"))
        
print("Number of attempts exceeds, you cannot log in to the system.")
