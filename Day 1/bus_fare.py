# importing the date class from the datetime module

from datetime import date


# Saving today's date in a variable
date = date.today()

# storing string literals representing days of the week in an array
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# initializing the fare
fare = 0

# getting and setting the days of the week to calculate the fare
day_number = date.weekday()
day = days[day_number]

# Setting the fare based on the day of the week
if day_number <= 4:
    fare = 100
elif day_number == 5:
    fare = 60
else:
    fare = 80

# printing the date, day and fare
print(f"Date: {date}\nDay: {day}\nFare: {fare}")
