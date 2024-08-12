# Input marks for three subjects
sub1 = int(input('Enter mark for subject 1: '))
sub2 = int(input('Enter mark for subject 2: '))
sub3 = int(input('Enter mark for subject 3: '))

# Constants for maximum marks
ONE_SUBJECT_MAX = 100
MAX_MARKS = 300

# Calculate total marks obtained and percentage
totalObtained = sub1 + sub2 + sub3
totalPercentage = (totalObtained / MAX_MARKS) * 100

# Calculate percentage for each subject
sub1_percentage = (sub1 / ONE_SUBJECT_MAX) * 100
sub2_percentage = (sub2 / ONE_SUBJECT_MAX) * 100
sub3_percentage = (sub3 / ONE_SUBJECT_MAX) * 100

# Check if each subject percentage is above 33% and total percentage is above 40%
if (sub1_percentage > 33) and (sub2_percentage > 33) and (sub3_percentage > 33) and (totalPercentage > 40):
    print("The student is pass")
else:
    print("The student failed.")
