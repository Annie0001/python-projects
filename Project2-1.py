# Programmer Name : Ani Ohanian
# Date: 7/30/22
# Description: This Program asks for the name, salary and the state for 6 employees. Calculates the federal tax, 
# state tax and the net salary for each employee.

# To calculate the federal tax, use the following criteria:

# If the salary is greater than 100,000 then calculate the federal tax at 20 percent.
# Otherwise calculate the federal tax at 15%.

# To calculate the state Tax, use the following criteria:
# If the employee is from CA, NV, AZ, or TX calculate the state tax at 10%
# Otherwise calculate the state tax at 12%

# Calculate and display the netsalary.
# Calculate the display the net salary of the employee. To calculate the net salary, subtract federal and state tax from the gross salary.

fedTaxPercentage20 = 0.2
fedTaxPercentage15 = 0.15
stateTaxPErcentage10 = 0.1
stateTaxPErcentage12 = 0.12

# Iterating and getting the details for each employee in every iteration
for i in range(6):

    employeeName = input("Please enter your name: ")

    #validating user salary input
    while(True):
        try:
            employeeGrossSalary = float (input("Please enter your gross salary: $"))
            while(employeeGrossSalary < 0):
                employeeGrossSalary = float(input("Please enter a non negative salary: $"))
            break
        except:
            print("You entered string for salary! Please enter an integer value for your salary.")


    employeeState = input ("Please eneter your state: ").upper()


    # Calculating the federal tax.
    if employeeGrossSalary > 100000 :
        fedTax = fedTaxPercentage20 * employeeGrossSalary 
    else:
        fedTax = fedTaxPercentage15 * employeeGrossSalary
    #Calculating the state Tax
    if employeeState == "CA" or employeeState == "NV" or employeeState == "AZ" or employeeState == "TX":
        stateTax = stateTaxPErcentage10 * employeeGrossSalary
    else:
        stateTax = stateTaxPErcentage12 * employeeGrossSalary
    #Calculating net salary
    netSalary = employeeGrossSalary - (fedTax + stateTax)
    print(employeeName + " your federal Tax is: $"+format(fedTax,'.2f')
    + " \nYour state tax is: $" +format(stateTax, '.2f')+ "\nYour net salary is $"+format(netSalary,'.2f'))
    print("\n")


