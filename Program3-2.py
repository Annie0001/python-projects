## Programmer Name : Ani Ohanian
# Date: 8/07/22
# Description: This program creates runners log based on each runners weekly mileage run.
# The runners: Mike, Tina, Jason, Vicky, and Tammy 
# are preparing for an upcoming marathon.
# Each day of the week, they run a certain number of miles and write them into a notebook. 
# At the end of the week, they would like to know the number of miles run each day, the total miles for the week,
# and average miles run each day, Write a program to help them analyze their data. Your program must contain parallel lists:
# a list to store the the names of the runners and a two-dimensional list of five rows and seven columns to store 
# the number of miles run by each runner each day.  

# Sample Output
# Name  Day 1   Day 2    Day 3    Day 4   Day 5   Day 6   Day 7   Average
# =========================================================================
# Mike   10.00   15.00    20.00    25.00   18.00    20.00    26.00    19.14
# Tina   15.00   18.00    29.00    16.00   26.00    20.00    23.00    21.00
# Jason  20.00   26.00    18.00    29.00   10.00    12.00    20.00    19.29
# Vicky  17.00   20.00    15.00    26.00   18.00    25.00    12.00    19.00
# Tammy 16.00    8.00     28.00    20.00   11.00    25.00    21.00    18.43

weekDays = ['Mon','Tue','Wed','Thur','Fri','Sat','Sun']
# creating 2D List
runnersData = []

# user input validation
while(True):
    try:
        numberOfRunners = int (input("Please enter for how many runners do you want to track their miles? "))
        if (numberOfRunners > 0):
            break
        else:
            print("Number should be more than zero.")
    except:
        print("Wrong input")

for runnerNumber in range (numberOfRunners):
    row = []
    totalMiles = 0
    # getting runner name
    runnerName = input("Please enter the runner"+str(runnerNumber+1)+"'s name: ")
    row.append(runnerName)
    for weekDay in weekDays:
        # validating miles for each day
        while(True):
            try:
                # getting runner miles
                miles = float (input("How many miles did "+ runnerName + " ran on "+ weekDay + "?"))
                if (miles >= 0):
                    break
                else:
                    print("Number should be zero or positive.")
            except:
                print("Wrong input. Please enter a number.")
        # adding miles for each day for every runner into the row list
        row.append(round(miles, 2))
        totalMiles += miles
        averageMiles = round(totalMiles / len(weekDays),2)
    row.append(round(totalMiles,2))
    row.append(round(averageMiles,2))
    runnersData.append(row) 

# printing table header 
print("Name", end="\t")
for weekDay in weekDays:
    print(weekDay , end="\t")
print("Total \t"+"Average")
print("=================================================================================")

# printing runner data
for runnerData in runnersData:
    for item in runnerData:
        print (item, end="\t")
    print("\n")

