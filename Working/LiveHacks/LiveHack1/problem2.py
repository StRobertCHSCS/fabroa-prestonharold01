'''
-------------------------------------------------------------------------------
Name:		pieces_chick.py
Purpose:	number  of pieces of chicken each student and teacher will recieve

Author:	Harold.P

Created:	02/10/2019
------------------------------------------------------------------------------
'''
# get number of pieces of chicken 
chicken = int(input("Enter the number of pieces of chicken: "))
# get number of students
students= int(input(" Enter number of students in the class: "))
# compute pieces of chicken each person recieves
pieces_chick= (chicken/students)
# compute number of pieces of chicken Mr.Fabroa will get (leftover)
fabroa_chicken= (chicken%students)
# output number of pieces of chicken each person will get
print(" The number of pieces of chicken each student will recieve is " + str(pieces_chick))
# output number of pieces of chicken Mr.Fabroa will recieve
print(" The number of pieces of chicken Mr.Fabroa will recieve is " + str (fabroa_chicken))
