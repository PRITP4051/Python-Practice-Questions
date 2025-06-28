# WAP that displays information about an employee. Use nested dictionary to 
# do the task. Also determine how to access an element in a nested dictionary 
# and how to add an element in nested dictionary.

D = {
    'emp1': {'name': 'PRIT', 'job': 'Mgr'},
    'emp2': {'name': 'DIRGH', 'job': 'Dev'},
}

# Accessing elements in a nested dictionary
print(D['emp1'].get('name'))
print(D['emp1'].get('job'))

# Adding a new nested dictionary for emp3
D['emp3'] = {}
D['emp3']['name'] = 'JAL'
D['emp3']['job'] = 'Janitor'
print(D)

# Adding another employee
D['emp4'] = {'name': 'MANNAT', 'job': 'Accountant'}
print(D)

# Removing emp3 and printing the result
x = D.pop('emp3')
print(D)
print(x)

# Displaying all employee information
for id, info in D.items():
    print("\nEmployee ID:", id)
    for key in info:
        print(key, ':', info[key])