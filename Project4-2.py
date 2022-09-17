# Programmer Name : Ani Ohanian
# Date: 8/14/22
# Description: This Program designs particular talent competition that has 5 judges, each of whom awards a score between 0 and
# 10 to each performer. Fractional scores, such as 8.3, are allowed. A performer’s ﬁnal score
# is determined by dropping the highest and lowest score received, then averaging the 3
# remaining scores. Write a program that uses these rules to calculate and display a
# contestant’s score. It should include the following functions:

# • getJudgeData() should ask the user for a judge’s score, store it in a 
# parameter variable, and validate it. This function should be called by main program once for each
# of the 5 judges.
# • calcScore(score1, score2, score3, score4, score5) should calculate and return the average of the 3 scores that
# remain after dropping the highest and lowest scores the performer received. This
# function should be called just once by main and should be passed the 5 scores.
# Two additional functions, described below, should be called by calcScore, which uses the
# returned information to determine which of the scores to drop.
# • findLowest(score1, score2, score3, score4, score5) should find and return the lowest of the 5 scores passed to it.
# NOTE: You are not allowed to use min() function
# • findHighest(score1, score2, score3, score4, score5) should find and return the highest of the 5 scores passed to it.
# NOTE: You are not allowed to use max() function



# this function validates negative user input 
def validateInput(userInput):
    if userInput < 0 or userInput > 10:
        print("Please re-enter the number between 0 to 10.")
        return False
    else:
        return True
    
# this function validates user input for float
def getAndValidateInputForFloat(inputString):
    while(True):
        try:
            userInput = float(input(inputString))
            if (validateInput(userInput)):
                return userInput
        except:
            print("Wrong input. Please re-enter the number between 0 to 10")
   

# this function gets the judge's score and stores in scores parameter
def getJudgeData(scores, scoreNum):
    judgesScore = getAndValidateInputForFloat("Please enter judge's score " + str(scoreNum + 1) + ": ")
    scores.append(judgesScore)

# this function gets 5 scores and calculates the max and min numbers by calling findhighest and findlowest functions.
# removes lowest and highest scores, calculates average, and returns average
def calcScore(score1, score2, score3, score4, score5):
    lowestScore = findLowest(score1, score2, score3, score4, score5)
    highestScore = findHighest(score1, score2, score3, score4, score5)
    scores.remove(lowestScore)
    scores.remove(highestScore)
    total = 0
    for item in scores:
        total += item
    averageScore = (round(total/len(scores),2))
    return averageScore

# this function finds and returns the lowest score
def findLowest(score1, score2, score3, score4, score5):
    min = score1
    if score2 < min:
        min = score2
    if score3 < min:
        min = score3
    if score4 < min:
        min = score4
    if score5 < min:
        min = score5
    return min

# this function finds and returns the highest score
def findHighest(score1, score2, score3, score4, score5):
    max = score1
    if score2 > max:
        max = score2
    if score3 > max:
        max = score3
    if score4 > max:
        max = score4
    if score5 > max:
        max = score5
    return max


scores = []
# to keep the program running until the user enters the correct input
toContinue = True
while(toContinue):
    print("Starting the Judge score program!")
    try:
        
        # calling getJudgeData function 5 times
        for scoreNumber in range(5):
            # calling getJudgeData function
            getJudgeData(scores, scoreNumber)

        # calling calcScore function 
        scoreCalculation = calcScore(scores[0], scores[1],scores[2],scores[3],scores[4])
        print("Your score is: " , scoreCalculation)
        toContinue = False
    except:
        print("Wrong input")