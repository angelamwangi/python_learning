#checks for conditions and executes if condition is met
#blood donation
'''body_weight=float(input("Enter your body weight in kgs: "))
age=int(input("Enter your current age: "))
if body_weight <=50 and age>15:
    print("Sorry,you cannot donate blood.")
else:
    print("Proceed to the next room")
'''
#########################GRADING SYSTEM#######################################
student_marks=int(input("Enter your marks: "))
if student_marks <30:
    print("Grade:E")
elif student_marks <40:
    print("Grade:D")
elif student_marks <50:
    print("Grade:C")
elif student_marks <60:
    print("Grade:B")
elif student_marks <=100:
    print("Grade:A")
elif student_marks>100:
    print("Invalid Input!")

