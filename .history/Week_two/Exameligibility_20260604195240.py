#A student can take an exam only if attendance is above 75% and fees are paid Otherwise explain why they cannot take the exam
#variables
attendance_percentage = 80
fees_paid = False
if attendance_percentage > 75 and fees_paid:
    print("You can take the exam")
else: print("You cannot take the exam because either your attendance is below 75% or you have not paid the fees")