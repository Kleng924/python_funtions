#Objective:
#The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, 
# and division.

#Task 1: Create functions for each arithmetic operation.
scores = [3, 5, 8, 9, 4]

print(int(5 + 9), (15 - 8), (2 * 6), (100/20))


#Task 2: Implement user input to receive numbers and an operation choice.

answer = input("What is the sum of 6 and 4?")
if answer == "10":
    print("That's right!")
if answer != "10":
    print("Try again!")


#Task 3: Ensure your program can handle division by zero and other potential errors.

a = 10
b = 0
if b == 0:
    print("Cannot divide by zero")
else:
    print(a/b)
