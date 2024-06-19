#Objective:
#The aim of this assignment is to create a program that tracks fitness activities and calories burned.

#Task 1: Develop a function to log different fitness activities and their duration. 
# For instance, activities = [’Dancing’, ‘Swimming’, ‘Biking’] and duration = [10, 20, 15] where 
# Dancing corresponds to 10 minutes, Swimming corresponds to 20 minutes, and Biking corresponds to 15 minutes.

activities = ['Dancing', 'Swimming', 'Biking']
durations = [10, 20, 15]

for i in range(len(activities)):
    activity = activities[i]
    duration = durations[i]
    
    print(f"{activity} {duration} minutes.")

input = input("Task 2.")
#Task 2: Write a simple function that estimates calories burned based on the activity and duration. For instance, 
# Total calories burned = Duration (in minutes)*3.5

activities = ['Dancing', 'Swimming', 'Biking']
durations = [10, 20, 15]

for i in range(len(activities)):
    activity = activities[i]
    duration = durations[i]
print(f"Total calories burned = {duration * 3.5}")


#Task 3: Create a summary function that provides a report of all activities and total calories burned for the day.

average_duration = sum(durations) 

calories_burned = (f"{average_duration * 3.5}")
print(f"Total calories burned = {calories_burned} for the day.")


