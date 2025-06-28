#Write a program that keeps name and phone numbers in a dictionary as key
# value pairs. 
# The program should display a menu that lets the user search a person’s 
# phone, add a new name and phone number, change an existing phone 
# number, and delete an existing name and phone number. 
#most imp
phonebook = {}
choice =1
while choice !=0:
    print('\n MENU')
    print('1. Add a record')
    print('2. Search a record')
    print('3. Change a record')
    print('4. Delete a record')
    print('5. Show All Records')
    print('0. Quit')
    choice =int(input("Enter your choice : "))
    if choice ==1:
        name =input("Enter name : ")
        phone =int(input("Enter 6 digit phone number : "))
        if name in phonebook:
            print("Name already exists")
        else:
            phonebook[name] = phone
            print('Record added')
    elif choice ==2:
        name =input("Enter name to search : ")
        if name in phonebook:
            print(name,' : ', phonebook[name])
        else:
            print('record not found')
    elif choice ==3:
        name =input('Enter name : ')
        if name in phonebook:
            phone =int(input("Enter 6 digit phone number : "))
            phonebook[name] = phone
            print('record updated')
        else:
            print('record not found')
    elif choice ==4:
        name =input('Enter name : ')
        if name in phonebook:
            del phonebook[name]
            print('Record deleted')
        else:
            print('record not found')
    elif choice ==5:
        for key,val in phonebook.items():
            print(key,":",val)
