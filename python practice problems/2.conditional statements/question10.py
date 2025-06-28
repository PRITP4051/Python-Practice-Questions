#WAP to read an angle from the user and then display its quadrant. 
# Program to read an angle and display its quadrant

angle = float(input("Enter the angle in degrees: "))

# Normalize angle to [0, 360)
angle = angle % 360

if angle == 0 or angle == 180 or angle == 360:
    print("The angle lies on the x-axis.")
elif angle == 90 or angle == 270:
    print("The angle lies on the y-axis.")
elif 0 < angle < 90:
    print("The angle is in the 1st quadrant.")
elif 90 < angle < 180:
    print("The angle is in the 2nd quadrant.")
elif 180 < angle < 270:
    print("The angle is in the 3rd quadrant.")
elif 270 < angle < 360:
    print("The angle is in the 4th quadrant.")