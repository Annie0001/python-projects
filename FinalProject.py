# Programer Name: Ani Ohanian
# Date:8/20/22
# Description: This program is called BankApp that simulates a banking application.
# The information needed for this project are stored in a text file. Those are:
# usernames, passwords, and balances.
# Your program should read username, passwords, and balances for each customer, and
# store them into three lists.
# userName (string), passWord(string), balances(float)
# The txt file with information is provided as UserInformtion.txt

# Example: This will demonstrate if file only contains information of 3 customers. You
# could add more users into the file.

# userName passWord    Balance
# ============================
# Mike     sorat1237#   350
# Jane     para432@4    400
# Steve    asora8731%   500

# When a user runs your program, it should ask for the username and password
# first. Check if the user matches a customer in the bank with the information
# provided. Remember username and password should be case sensitive.
# After asking for the user name, and password display a menu with the following
# options and ask the user for input (Use a While Loop). 

# for quiting the program
quitProgram = ""

# openning the file in read and write mode
fileReadWrite = open("UserInformtion.txt",'r+') 
# keeping usernames in this list
userNames =[]
# keeping passwords in this list
passWords = []
# keeping balances in this list
balances = []

# defining this varible to keep the username that is using this program 
userInputName = ""
# defining this varible to keep the password that is using this program 
userInputPassword =""

# this function is used to deposite the given parameter amount
def deposit(depositAmount):
    userNameIndex = userNames.index(userInputName) 
    userBalance = balances[userNameIndex] 
    depositPlusNewBalance = depositAmount + userBalance
    balances[userNameIndex]= depositPlusNewBalance
    showBalance()

# this function is used to withdraw the given parameter amount
def withdraw(withdrawAmount):
    userNameIndex = userNames.index(userInputName) 
    userBalance = balances[userNameIndex] 
    withdrawnNewBalance = userBalance - withdrawAmount
    balances[userNameIndex]= withdrawnNewBalance   
    showBalance()

# this function is used to get the balance of the current user
def getBalance():
    userNameIndex = userNames.index(userInputName)
    userBalance = balances[userNameIndex] 
    return userBalance

# this function is used to show the balance of the current user
def showBalance():
    userNameIndex = userNames.index(userInputName)
    userBalance = balances[userNameIndex]
    print("Your balance is: $"+format(userBalance, '.2f'))

# this function is used to change from one user to another
def changeUser():
    # calling the userNamePasswordCheck function to ask for username and password
    userNamePasswordCheck()

# this function is used to add new user
def addNewClient():
    newUsersName = input("Please enter your prefered username:")
    newUsersPassword = input("Please enter your prefered password: ")
    while True:
        try:
            newUsersBalance = float(input("Please enter the amount you would like to put into your account:$ "))
            if newUsersBalance < 0:
                print("Please enter zero or a positive number.")
            else:
                break
        except:
            print("Wrong input.")

    # adding the new user's username, password, and balance to the list
    userNames.append(newUsersName)
    passWords.append(newUsersPassword)
    balances.append(newUsersBalance)

# this function asks for username and password and checks to see if the username ands password is valid
def userNamePasswordCheck():
    global userInputName
    global userInputPassword 
    while(True):
        userInputName = input("Please enter your username: ")
        if userInputName in userNames:
            break
        else:
            print("Please enter correct username.")
    
    while(True):
        userInputPassword = input("Please enter your password: ")   
        nameIndex = userNames.index(userInputName)
        passwordItem =passWords[nameIndex]
        if userInputPassword == passwordItem:
            return True
        else:
            print("Please enter correct password. ")

# reading from the file line by line and keeping usernames, passwords, and balances in the appropriate lists
for i in fileReadWrite:
    lineItem = i.split()
    userNames.append(lineItem[0])
    passWords.append(lineItem[1])
    balances.append(float(lineItem[2]))


print("Welcome to BankApp!")

# check for the username and password then show the menu
if userNamePasswordCheck():
    while(quitProgram != "YES"):
        menuOption = input("Type D to deposit money\nType W to withdraw money\nType B to display Balance\n"+
        "Type C to change user, display user name\nType A to add new client \nType E to exit \n ").upper()

        if (menuOption == "D"):
            while True:
                try:
                    # getting deposit amount and validating
                    userDepositeAmount = float(input("Please enter your deposit amount: $"))
                    if userDepositeAmount <= 0:
                        print("Please enter a positive number.")
                    else:
                        break
                except:
                    print("Wrong input.")
            #calling deposit function
            deposit(userDepositeAmount)

        elif (menuOption == "W"):
            showBalance()
            while True:
                try:
                    # getting withdraw amount and validating
                    userWithdrawAmount = float(input("Please enter the amount you want to withdraw: $"))
                    if userWithdrawAmount <= 0:
                        print("Please enter a positive number.")
                    else:
                        break
                except:
                    print("Wrong input.")
            
            currentBalance = getBalance()
            # check the user withdraw amount whether it is less than or equal to the current balance
            if userWithdrawAmount <= currentBalance:
                #calling withdraw function
                withdraw(userWithdrawAmount)
            else: 
                print("You don't have enough balance to withdraw.")
        elif (menuOption == "B"):
            #calling balance function
            showBalance()
        elif (menuOption == "C"):
            #calling change user function, and ask for username and password
            changeUser()
        elif (menuOption == "A"):
            #calling add new client function
            addNewClient()
        elif (menuOption == "E"):
            #exit the program
            quitProgram = "YES"
            # Reposition pointer at the beginning of the file
            fileReadWrite.seek(0)
            # going through the lists (username, password, and balance) and writting each to the same file that we read from
            for i in range(len(userNames)):
                user = userNames[i]
                password = passWords[i]
                balance = balances [i]
                fileReadWrite.write(str(user)+" "+str(password)+" "+format(balance, '.2f')+"\n")
            # using truncate to cleanup the old content of the file    
            fileReadWrite.truncate()
            # closing the file
            fileReadWrite.close()
        else:
            print("Invalid option. Please enter the correct option.")
