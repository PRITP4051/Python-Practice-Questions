# WAP that has dictionary of names of students and a list of their marks in 4 
# subjects. Create another dictionary from this dict that has names of the 
# students and their total marks. Find out the topper and his/her score.
Marks = {'Dirgh': [97,89,94,90],'Prit':[92,91,93,95],'Ansh':[67,99,88,90]}
tot =0
Total_marks =dict()
for key,value in Marks.items():
    tot =sum(value)
    Dict = {key : tot}
    Total_marks.update(Dict)
print(Total_marks)
max =0
Topper =''
for key,value in Total_marks.items():
    if value > max:
        max = value
        Topper = key
print("Topper is : ", Topper," with marks = ", max)

