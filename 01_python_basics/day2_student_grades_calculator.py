
name = input('Enter your name: ')
total_number_subjects = int(input('Enter total number of subjects: '))
marks = []
total_marks = total_number_subjects * 100
while total_number_subjects:
    sub_marks = int(input("Enter marks: "))
    marks.append(sub_marks)
    total_number_subjects -= 1
total_marks_secured = sum(marks)
print(total_marks_secured)

percentage = (total_marks_secured / total_marks) * 100
print(percentage)

if percentage >= 90:
    print("You have been awarded Grade A")
elif percentage >= 80:
    print("You have been awarded Grade B")
elif percentage >= 70:
    print("You have been awarded Grade C")
elif percentage >= 60:
    print("You have been awarded Grade D")
else:
    print("You have been awarded Grade F")