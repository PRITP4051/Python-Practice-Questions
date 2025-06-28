#  WAP that  
# a) Store correct password in a variable. 
# b) Asks user to enter his/her password. 
# c) Validate the two passwords: 
# a. Check if user has entered password. If not, then give message “Please 
# enter your password.” 
# b. Check if both passwords are same. If they are same, show message 
# “Correct! The entered password matches the original password.” 
# c. Show “Incorrect password” otherwise  

password="prit@2005"
n=input("enter the password")
if n=="":
    print("please enter your password")
elif n==password:
    print("correct! The entered password matches the original password." )
else:
    print("Incorrect password")