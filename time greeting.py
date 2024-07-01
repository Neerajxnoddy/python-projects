import datetime

# Get the current time
now = datetime.datetime.now()
print("curernt time=",now)
# Determine the greeting based on the time of day
if now.hour < 12:
    greeting = "Good morning"
elif 12 <= now.hour < 17:
    greeting = "Good afternoon"
else:
    greeting = "Good evening"

# Get the user's name
name = input("What is your name? ")

# Print the greeting
print(greeting + ", " + name + "!")