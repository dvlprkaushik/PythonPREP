# Initialize an empty list
studentMarks = []

# Collect marks for 7 students and append them to the list
mark1 = float(input('Enter marks for student 1: '))
studentMarks.append(mark1)

mark2 = float(input('Enter marks for student 2: '))
studentMarks.append(mark2)

mark3 = float(input('Enter marks for student 3: '))
studentMarks.append(mark3)

mark4 = float(input('Enter marks for student 4: '))
studentMarks.append(mark4)

mark5 = float(input('Enter marks for student 5: '))
studentMarks.append(mark5)

mark6 = float(input('Enter marks for student 6: '))
studentMarks.append(mark6)

mark7 = float(input('Enter marks for student 7: '))
studentMarks.append(mark7)

studentMarks.sort()
print(studentMarks)
