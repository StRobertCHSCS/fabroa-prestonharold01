"""
*******************************************************************************
Filename:       livehack_2.py
Description:    Determine the type of triangle based on angles
Author:         Harold.P
Created On:     18/11/2019
*******************************************************************************
"""
# get interior angles
angle1 = int(input("Enter the first angle: "))
angle2 = int(input("Enter the second angle: "))
angle3 = int(input("Enter the thrid angle: "))

# compute addition
add1 = angle1 + angle2 +angle3

# determine the type of triangle
if (angle1 + angle2 + angle3 = 180) and ((angle2 == angle3) or (angle1 == angle2) or (angle1 == angle3))
    print(" A triangle with angles " + str(angle1) + ", " == str(angle2) + ", or" + str(angle2) + ", " == str(angle3) + ", or" + str(angle1) + ", " == str(angle3) + " forms an Isosceles triangle")
elif (angle1 + angle2 + angle3 = 180) and ((angle2 != angle3) or (angle1 != angle2) or (angle1 != angle3))
 print(" A triangle with angles " + str(angle1) + ", " != str(angle2) + ", or" + str(angle2) + ", " != str(angle3) + ", or" + str(angle1) + ", " != str(angle3) + " forms a Scalene triangle")
else:
     print(" Error the angles do not form a triangle")

# determine if the triangle is equilateral
 if (angle1 + angle2 + angle3 = 180) and ( angle1==angle2==angle3 ==60)
    print("The triangle is an Equilateral triangle")

