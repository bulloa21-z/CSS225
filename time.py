# Debugged by Bryan Ulloa

# 10/23/2023

currentTimeStr = input("What is the current time (in hours 0-23)?")
waitTimeStr = input("How many hours do you want to wait?")

currentTimeInt = int(currentTimeStr)
waitTimeInt = int(waitTimeStr)

finalTimeInt = currentTimeInt + waitTimeInt
print(finalTimeInt)
