# Programmer Name : Ani Ohanian
# Date: 7/31/22
# Description: This Program calculates and prints the bill for a cellular telephone company. 
# A telephone company offers two types of service: regular and premium. 
# Its rate varies, depending on the type of service. The rates are compared as follows.

# Regular service:  $10.00 plus the first 50 minutes are free. Charges for over 50 minutes are $0.20 per minute.
# Premium service:  $25 plus:

# For calls made from 6:00 a.m. to 6:00 p.m., the first 75 minutes are free; charges for more than 75 minutes are $0.10 per minute
# For calls made from 6:00 pm to 6:00 a.m., the first 100 minutes are free; charges for more than 100 minutes are $0.05 per minute.
# Your program should prompt the user to enter an account number, a service code (type character), and the number of minutes the service was used. 
# A service code of r or R means regular service; a service code of p or P means premium service. Treat any other character as an error. 
# Your program should output the account number, type of service, number of minutes the telephone service was used, and the amount due from the user.

# For the premium service, the customer may be using the service during the day and the night. Therefore, to calculate the bill, 
# you must ask the user to input the number of minutes the service was used during the day and the number of minutes the service was used during the night.

# This program validates user input for negative values and loop until the user enters the correct entry. 
# Also, using a loop make sure to ask if the user wants to continue with the program or not. 
# If the user enters YES, the program should continue else, the program will exit.
continueProgram = 'YES'
billDay = 0
billNight = 0
bill = 0

while continueProgram == 'YES':
    # Considering account number can contain any characters. Thus, no validation.
    accountNumber = input("Please enter your account number: ")
    print("\t")
    serviceCode = input('Please enter your service code ("R" for Regular service and "P" for Premium Service.): ').upper()
    print("\t")

    if serviceCode == 'R':
        #validating user input for string
        while(True):
            try:
                numOfMin = int(input("Please enter the number of minutes used: "))
                while (numOfMin < 0):
                    numOfMin = int (input("Please enter a non negative number for number of minutes used: "))
                break
            except:
                print("You entered wrong value for number of minutes.")
        
        print("\t")
        if numOfMin >50:
            bill = 10 + ((numOfMin-50) * 0.20)     
        else:
            bill = 10   
        print("Your bill is: $", round(bill,2))

    elif serviceCode == 'P':
        #validating user input for string
        while(True):
            try:
                numMinDay = int(input("Please enter the number of minutes you used during the day (6a.m. - 6p.m.): "))
                while (numMinDay < 0):
                    numMinDay = int (input("Please enter a non negative number for the number of minutes you used during the day (6a.m. - 6p.m.): "))
                print("\t")
                break
            except:
                print("You entered wrong value for number of minutes used during the day.")


        #validating user input for string
        while(True):
            try:
                numMinNight = int(input("Please enter the number of minutes you used during the night (6p.m. - 6 a.m.): "))
                while (numMinNight < 0):
                    numMinNight = int (input("Please enter a non negative number for the number of minutes you used during the night (6p.m. - 6a.m.): "))
                print("\t")
                break
            except:
                print("You entered wrong value for number of minutes used during the night.")
            

        if numMinDay > 75:
            billDay = (numMinDay-75) * 0.10
            print("The amount of your day bill is: $", round(billDay,2))
        else:
            print("The amount of your day bill is 0. ")

        if numMinNight >100:
            billNight = (numMinNight-100) * 0.05
            print("The amount of your night bill is: $", round(billNight,2))
        else: 
            print("The amount of your night bill is 0. ")
        bill = 25 + billDay + billNight
        print("The amount of your bill is $", round(bill,2))

    else:
        # To let the user know about the wrong input for service code
        print("Error! You entered a wrong service code. The service code should be either 'R' or 'P' ")

    continueProgram = input("Do you like to continue with the program or not. Enter YES to continue, enter anything else to exit: ").upper()