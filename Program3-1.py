# Programmer Name : Ani Ohanian
# Date: 8/06/22
# Description: This program creates a menu to allow the user to add, insert, remove, find the maximum, the minimum, 
# and sort the list in descending order (larger to smaller value). Declare your list as the list of strings.
# studentFullName=["Mike navarro","Miguel saba","Maria Rami"]
# You may use any of the built-in functions. Here is a sample output:
# 1- Add an item to the list
# 2- Remove an item from the list
# 3- Insert an item into the list
# 4- Find maximum
# 5- Find Minimum
# 6- Sort the list in descending order
# 7- Quit the program
# Please enter your option: 3
# Where do you want to insert the item? (Enter the index number) 1
# Please enter the value for the item you want to insert: "Tina Mari"
# Your original List : ["Mike navarro","Miguel saba","Maria Rami"]
# After inserting an item into index 1:
# ["Mike navarro","Tina Mari", "Miguel saba","Maria Rami"]
# Once the user enters an option, your program should execute the code for that option and displays the list 
# before and after the operations. 
# Make sure to use a while loop so the program runs until user enters the quit option.


# This variable is used to know when to quit the program 
quit_program = ""
# original list of names
studentFullNames=["Mike navarro","Miguel saba","Maria Rami"]
print(studentFullNames)

while quit_program != "YES":

    print("\n1- Add an item to the list\n"+"2- Remove an item from the list\n"+"3- Insert an item into the list\n"+"4- Find maximum\n"
    +"5- Find Minimum\n"+"6- Sort the list in descending order\n"+"7- Quit the program")

    try:
        # getting option from the user
        optionNumber = int(input("Please enter your option number from the menu above: "))
        # add option
        if optionNumber == 1:
            addItem = input("Please enter the value for the item you want to add to the list: ")
            print("Before operation:", studentFullNames)
            studentFullNames.append(addItem)
            print("After operation:", studentFullNames)
        # remove option
        elif (optionNumber == 2):
            removeItem = input("Please eter the name that you would like to remove from the list: ")
            print("Before operation:", studentFullNames)
            studentFullNames.remove(removeItem)
            print("After operation:", studentFullNames)
        # insert in a specific index option
        elif (optionNumber == 3):
            insertIndex = int(input("Where do you want to insert the item? (Enter the index number)"))
            insertItemName = input("Please enter the value for the item you want to insert:" )
            print("Before operation:", studentFullNames)
            studentFullNames.insert(insertIndex,insertItemName)
            print("After operation:", studentFullNames)
        # finding max
        elif (optionNumber == 4):
            print(studentFullNames)
            print("Maximum is:", max(studentFullNames))
        # finding min
        elif (optionNumber == 5):
            print(studentFullNames)
            print("Minimum is:", min(studentFullNames))
        # sorting in desending order
        elif (optionNumber == 6):
            print("Before operation:", studentFullNames)
            studentFullNames.sort(reverse = True)
            print("After operation:", studentFullNames)
        # quit
        elif(optionNumber == 7):
            quit_program = "YES"
        # if wrong option is selected such as: less than 1 and more than 7
        else:
            print("Wrong option number")
    except:
        # checking any wrong input such as string for option number
        print("Wrong input")


