# Programmer Name : Ani Ohanian
# Date: 7/23/22
# Description: This Program will ask the student for  3 exam scores.
# Calculate the average score.
# Using a bunch of IF conditions, the computer should determine the grade and display the grade to the user. Use the following Criteria:
# If Average is 98-100… Assign the grade “A+”
# If Average is 95-97… Assign the grade “A”
# If Average is 91-94… Assign the grade “A-”
# If Average is 88-90… Assign the grade “B+”
# If Average is 84-87… Assign the grade “B”
# If Average is 80-83… Assign the grade “B-”
# If Average is 75-79… Assign the grade “C+”
# If Average is 70-74… Assign the grade “C”
# If Average is less than 70 and greater than 60 assign grade “D”
# If Average is less than or equal 60 assign grade "NC"
# Display the student name 
# Display the Average score and letter grade back to the student.

studentName = input("Please enter your name: ")

score1 = float(input("Please enter your 1st exam score: "))
if (score1 < 0 or score1 > 100):
    print("1st exam score is out of range. Please enter a valid score.")
    exit()

score2 = float(input("Please enter your 2nd exam score: "))
if (score2 < 0 or score2 > 100):
    print("2nd exam score is out of range. Please enter a valid score.")
    exit()

score3 = float(input("Please enter your 3rd exam score: "))
if (score3 < 0 or score3 > 100):
    print("3rd exam score is out of range. Please enter a valid score.")
    exit()

averageScore = float ((score1 + score2 + score3) / 3)

letterGrade = ""
if (averageScore >= 98 and averageScore <= 100):
    letterGrade = '"A+"'

elif (averageScore >= 95):
    letterGrade = '"A"'

elif(averageScore >= 91):
    letterGrade = '"A-"'

elif(averageScore >= 88):
    letterGrade = '"B+"'

elif(averageScore >= 84):
    letterGrade = '"B"'

elif(averageScore >= 80):
     letterGrade = '"B-"'

elif(averageScore >= 75):
    letterGrade = '"C+"'

elif(averageScore >= 70):
    letterGrade = '"C"'

elif(averageScore > 60):
    letterGrade = '"D"'

else:
    # this means the average score is less than or equal to 60
    letterGrade = '"NC"'

print(studentName,"your average score is", round(averageScore, 2), "and your letter grade is", letterGrade)