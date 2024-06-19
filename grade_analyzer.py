#Objective:
#The aim of this assignment is to analyze a set of grades and provide statistics.

#Task 1: Code a function to calculate the average grade.

grades = [80, 95, 100, 76, 86]

def average(grades):
    return sum(grades) / len(grades)

grade_average = average(grades)

print(grade_average)

#Task 2: Implement a function to find the highest and lowest grade.

print(max(grades))
print(min(grades))

#Task 3: Create a feature that categorizes grades into letter grades (A, B, C, etc.).


grades = [80, 95, 100, 76, 86]
user_input = input(grades)

if grades >= "90":
    print("A")
if grades >= "80":
     print("B")
if grades >= "70":
    print("C")










