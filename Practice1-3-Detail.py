# Programer Name: Ani Ohanian
# Date:7/21/22
# Description: This program will be used to design a mobile phone app which allows a user to press a button that starts a 
# timer that counts seconds.When the user presses the button again, the timer stops. After drawing the flowchart and 
# write pseudocode,code the program that accepts the elapsed time in seconds and displays the value in minutes and 
# remaining seconds.For example, if the elapsed time was 130 seconds, the output would be 2 minutes and 10 seconds.

import time

elapseTimeInSeconds = int(input("Please press any key to start the timer"))

# # get current time in seconds
# t = time.time()
# startTime = t
# print ("Timer started.")

# stopTimeKey = input("Please press any key to stop the time")

# t = time.time()
# stopTime = t
# print("Timer stopped.")

#elapseTimeInSeconds = stopTime - startTime

# used for debugging
# print("Elaps Time in Seconds" , elapseTimeInSeconds)

elapseTimeMinutes = int(elapseTimeInSeconds // 60)
elapseTimeSeconds = int(elapseTimeInSeconds % 60)

print("elapsed time is: ",elapseTimeMinutes , "minutes","and",elapseTimeSeconds,"seconds")

