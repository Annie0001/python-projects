# Programmer Name : Ani Ohanian
# Date: 7/23/22
# Description: This Program will collect the following data from the user:
# 1)    User last name
# 2)    User First Name
# 3)    Number of Hours Worked.
# 4)    Hourly-wage
 
# Calculate the gross wage based on the formula:
# Gross wage is number of hours worked multiplied by hourly-wage.
# Hint: You use the symbol * for multiplication.
# Output: Display the user name and gross wage.

lastName = input("Please enter your last name: ")
firstName = input("Please enter your first name: ")
hoursWorked = float (input("Please enter your worked hours: "))
if (hoursWorked < 0):
    print("Please enter valid worked hours.")
    exit()
hourlyWage = float (input("Please input your hourly wage: $"))
if (hourlyWage <= 0):
    print("Please enter valid hourly wage.")
    exit()

grossWage = hoursWorked * hourlyWage

print(firstName, "your gross wage is: $" + format(grossWage,'.2f'))


