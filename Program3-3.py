# Programmer Name : Ani Ohanian
# Date: 8/08/22
# Description: This program determines the length of bursts of zero’s in a list of N numbers stored in an List.
# The program should record the length of the bursts of zero’s in another List. The program should then print the lengths of the bursts.
# Using this second List with the lengths of the bursts, it should also compute and print the following:
# the average length of the bursts, the minimum burst length, the maximum burst length, and the total number of zeros (the sum of the burst lengths). 
# Your program should:
# 1. Prompt the user for the size of the list (N). Then it should prompt the user to enter N numbers and store them into a list called burstList. 
#    Note, you should specify the maximum size of N allowed (based on how large you declare your List).
# 2. Given N and list, your program should compute the lengths of the bursts of zeros and store them in a list called BurstLengths. Use a for loop in this step.
# 3. Given the BurstLengths List , use a while loop to print the list of burst lengths. Format this nicely in a table with headings.
# 4. Given the BurstLengths List , compute and then print the following information:
# a. Average burst length
# b. Minimum burst length
# c. Maximum burst length
# d. Total number of zeros
# Example data and results:
# N (entered by the user and stored in N): 15
# List of numbers (entered by the user and stored in list):
# 1, 0, 0, 0, 0, 3, 7, 0, 0, 0, 0, 0, 0, 50, 0
# List of bursts (computed by your program and stored in BurstList): 4, 6, 1
# Average burst length (computed by your program): 3.67
# Minimum burst length (computed by your program): 1
# Maximum burst length (computed by your program): 6
# Total number of zeros (computed by your program): 11
# Results:
# Burst   Length

# 1             4

# 2             6

# 3             1

# Average burst length: 3.67
# Minimum burst length: 1
# Maximum burst length: 6
# Total number of zeros: 11


# user input validation for list of numbers length
while(True):
    try:
        userInputListSize = int(input("This program will compute burst of zeros. Please enter how many numbers do you like to add to the list? "))
        if (userInputListSize > 0):
            break
        else:
            print("Number should be more than zero.")
    except:
        print("Wrong input. Please enter a positive integer number.")

burstList=[]
burstLength=[]
# this variable is used for counting number of zeros in each burst
counter = 0
total = 0
averagebursts = 0

# looping through list of numbers length
for number in range(userInputListSize):
    # input validation for each number
    while(True):
        try:
            userInput = int(input("Please enter integer number to insert into this list: "))
            break
        except:
            print("Wrong input")
    # adding the number to burst list
    burstList.append(userInput)

print(burstList)

# looping through burst list
for i in burstList:
    # when an item is equal to zero in the list, it adds 1 to the counter
    if i == 0:
        counter += 1
    else:
        if counter != 0:
            # adding the burst count to the burst length only if we already counted number of zeros
            burstLength.append(counter)
            # reseting the counter
            counter = 0
# adding zeros count if the burst list is ending with zeros
if counter != 0:
    burstLength.append(counter)

print("Burst\tLength")
burstNumberIndex = 0
# looping through burst length
while(burstNumberIndex < len(burstLength)):
    # calculating total number of zeros
    total += burstLength[burstNumberIndex]
    print(burstNumberIndex+1,"\t", burstLength[burstNumberIndex])
    burstNumberIndex+=1

# doing calculations if the burst list has zeros
if (total != 0):
    averagebursts = total / len(burstLength)
    print("Average burst length:", round(averagebursts, 2))
    print("Minimum burst length:", min(burstLength))
    print("Maximum burst length:", max(burstLength))

# no calculations in case of no zeros in burst list
else:
    print("Average burst length cannot be calculated")
    print("Minimum burst length cannot be calculated")
    print("Maximum burst length cannot be calculated")
print("Total number of zeros:", total)





