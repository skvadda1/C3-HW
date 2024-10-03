workingDays = int(input("Total Number of Working Days: "))
daysAbsent = int(input("Total Number of Days Absent: "))

percentage = 100 * float(daysAbsent)/float(workingDays)

if percentage < 75:
    print("Student is eligible to sit in examination room")
else:
    print("Student is not eligible to sit in examination room")