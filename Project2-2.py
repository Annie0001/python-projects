
# Programmer Name : Ani Ohanian
# Date: 7/30/22
# Description: This Program helps Professor Navi to calculate the average score and letter grade for his students in CS119. 
# It asks how many students Professor Navi has in his CS119. Using loop it asks for the following data:

# The student name.
# Scores of the 3 exams.
# Calculates the average score.
# Using a bunch of IF conditions, the computer should determine the grade and display the grade to the user. Use the following Criteria:
#  If Average is 98-100… Assign the grade “A+”
#  If Average is 95-98… Assign the grade “A”
#  If Average is 91-95… Assign the grade “A-”
# If Average is 88-91… Assign the grade “B+”
#  If Average is 84-88… Assign the grade “B”
#  If Average is 80-84… Assign the grade “B-”
# If Average is 75-80… Assign the grade “C+”
#  If Average is 70-75 Assign the grade “C”
#  If Average is less than 70 and greater than 60 assign grade “D”
#  If Average is less than or equal 60 assign grade "NC"
# Display the student name and the grade back to the user.

# Validating number of students
while(True):
    try:
        totalNumOfStudents = int(input("Please enter the total number of students in your CS119 class: "))
        while(totalNumOfStudents < 0):
            totalNumOfStudents = int(input("Please enter a non negative number of students: "))
        break
    except:
        print("You entered wrong value for number of students!")

# Iterating through the number of students
for studentNumber in range(totalNumOfStudents):

    studentName = input("Please enter student " + str(studentNumber+1)+ " name: ")
    # inputting / checking /validating score 1
    while(True):
        try:
            score1 = float(input("Please enter student's 1st exam score between 0 to 100: "))
            while (score1 < 0 or score1 > 100):
                score1 = float(input("1st exam score is out of range. Please enter a valid score between 0 to 100: "))
            break
        except:
            print("You entered wrong value for exam score!")

    # inputting / checking / validating score 2
    while(True):
        try:
            score2 = float(input("Please enter student's 2nd exam score between 0 to 100: "))
            while (score2 < 0 or score2 > 100):
                score2 = float(input("2nd exam score is out of range. Please enter a valid score between 0 to 100: "))
            break
        except:
            print("You entered wrong value for exam score!")

     # inputting / checking / validating score 3
    while(True):
        try:
            score3 = float(input("Please enter student's 3rd exam score between 0 to 100: "))
            while (score3 < 0 or score3 > 100):
                score3 = float(input("3rd exam score is out of range. Please enter a valid score between 0 to 100: "))
            break
        except:
            print("You entered wrong value for exam score!")

    #calculating average score
    averageScore = float ((score1 + score2 + score3) / 3)

    # conditional statements to determine the student grade 
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

    # displaying the student name, average score, and the letter grade
    print(studentName,"your average score is", round(averageScore, 2), "and your letter grade is", letterGrade)