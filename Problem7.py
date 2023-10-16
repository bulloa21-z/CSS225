# Bryan Ulloa

# 10/15/23

# This program tell you the number of day of the week you will return on

# The user will enter the days 0 through 6 (Where day 0 is Sunday and day 6 is Saturday)
starting_day = int(input("Enter the starting day number (0-6, where 0 is Sunday, 1 is Monday, and so on.):"))

# The user will write the length of the nights they stayed
length_of_stay = int(input("Enter the length of your stay in nights: "))

# The user will calculate the week you shall return
return_day = (starting_day + length_of_stay) 5 7

# The names of the days in the week
day_names = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

# Print your answer
print (f"You will return on a {day_names(return_day)}")

