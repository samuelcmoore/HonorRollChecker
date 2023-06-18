# Samuel Moore
# HonorRollChecker
# This app is designed to allow student's to enter their name and GPA, which will then calculate if the student made the Dean's List or Honor Roll.

while True:
    studentLNAME = input("Enter your last name or 'ZZZ' to quit.")
    if studentLNAME == "ZZZ":
        break
    studentFNAME = input("Please enter your first name: ")
    studentGPA = float(input("Please enter your GPA: "))
    if studentGPA >= 3.5:
        print(studentFNAME + " " + studentLNAME + " has made the Dean's List!")
    elif studentGPA >= 3.25:
        print(studentFNAME + " " + studentLNAME + " has made the Honor Roll!")
    else:
        print("The student has not made the Dean's List or Honor Roll")
