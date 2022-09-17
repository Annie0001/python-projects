# Programmer Name : Ani Ohanian
# Date: 8/14/22
# Description: This Program creates a menu to allow the user to add, insert, remove, find the maximum,
# the minimum, and sort the list in descending order (larger to smaller value). Declare your list as list of string.

# studentFullName=["Mike navarro","Miguel saba","Maria Rami"]
# You may only use these build in functions len(), index(). Here is an sample output:

# 1- Add an item to the list  ..........addItem(item) 
# 2- Remove item from the list .......removeItem(item)
# 3- Insert an item to the list .....insertToList(item, index)
# 4- Find maximum ....findMax(list)
# 5- Find Minimum ....findMin(list)
# 6- Sort the list in descending order .....sortList(list)
# 7- Display the list.... displayList(list)
# 8- Quit the program .....exit()

# Please enter your option: 3 
# Where do you want to insert the item? (Enter the index number) 1
# Please enter the value for the item you want to insert: "Tina Mari"
# Your program should call the function  insertToList(item, index)
# Your original List : ["Mike navarro","Miguel saba","Maria Rami"]
# After inserting an item into index 1:
# ["Mike navarro","Tina Mari", "Miguel saba","Maria Rami"]
# Once the user enters an option, your program should execute the code for that option and displays the list before and after the operations.
# Make sure to use a while loop so the program runs until user enters the quit option.
# For this program, you have to write your own functions for lists without using any of the build-in functions. 

# This variable is used to know when to quit the program 
quit_program = ""
studentFullNames=["Mike navarro","Miguel saba","Maria Rami"]
print(studentFullNames)

def addItem(item):
    global studentFullNames
    newItemArray = [item]
    studentFullNames += newItemArray

def removeItem(item):
    global studentFullNames
    index = studentFullNames.index(item)
    del studentFullNames[index]

def insertToList(item, index):
    global studentFullNames
    newArray = [""] * (len(studentFullNames) + 1)
    j = 0
    for i in range(len(studentFullNames)):
        if i == index:
            newArray[j] = item
            j+=1
            newArray[j] = studentFullNames[i]
        else:
            newArray[j] = studentFullNames[i]
        j+= 1
    studentFullNames = newArray

def findMax(list):
    maxItem = list[0]
    for item in list:
        if item > maxItem:
            maxItem = item
    return maxItem

def findMin(list):
    minItem = list[0]
    for item in list:
        if item < minItem:
            minItem = item
    return minItem

def sortList(list):
    global studentFullNames
    newList = [""]* len(list)
    for i in range(len(list)):
        max = findMax(list)
        newList[i] = max
        del list[i]

    studentFullNames = newList    

def displayList(list):
    print("Display the list: ", list)

def exit():
    global quit_program
    quit_program = "YES"
    
while quit_program != "YES":

    print("\n1- Add an item to the list\n"+"2- Remove an item from the list\n"+"3- Insert an item into the list\n"+"4- Find maximum\n"
    +"5- Find Minimum\n"+"6- Sort the list in descending order\n"+"7- display the list\n"+"8- Quit the program")
    
    try:
        # getting option from the user
        optionNumber = int(input("Please enter your option number from the menu above: "))

        if optionNumber == 1:
            userInput = input("Please enter the value for the item you want to add to the list: ")
            print("Before operation:", studentFullNames)
            addItem(userInput) 
            print("After operation:", studentFullNames)
        # remove option
        elif (optionNumber == 2):
            userInput = input("Please enter the name that you would like to remove from the list: ")
            print("Before operation:", studentFullNames)
            removeItem(userInput)
            print("After operation:", studentFullNames)
        # insert in a specific index option
        elif (optionNumber == 3):
            insertIndex = int(input("Where do you want to insert the item? (Enter the index number)"))
            insertItemName = input("Please enter the value for the item you want to insert:" )
            print("Before operation:", studentFullNames)
            insertToList(insertItemName,insertIndex)
            print("After operation:", studentFullNames)
        # finding max
        elif (optionNumber == 4):
            print(studentFullNames)
            print("Maximum is:", findMax(studentFullNames))
        # finding min
        elif (optionNumber == 5):
            print(studentFullNames)
            print("Minimum is:", findMin(studentFullNames))
        # sorting in desending order
        elif (optionNumber == 6):
            print("Before operation:", studentFullNames)
            studentFullNames.sort(reverse = True)
            print("After operation:", studentFullNames)
        # Display the list
        elif (optionNumber == 7):
            displayList(studentFullNames)        
        # quit
        elif(optionNumber == 8):
            exit()
        # if wrong option is selected such as: less than 1 and more than 7
        else:
            print("Wrong option number")
    except:
        # checking any wrong input such as string for option number
        print("Wrong input")