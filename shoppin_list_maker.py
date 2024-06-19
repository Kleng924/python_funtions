#Objective:
#The aim of this assignment is to create a program that helps users make a shopping list.

#Task 1: Write a function that lets the user add items to a list.

shopping_list = ["milk", "banana", "water", "eggs"]
shopping_list.append("bread")

print(shopping_list)

#Task 2: Include a feature to remove items from the list.

shopping_list_2 = ["milk", "banana", "water", "eggs", "bread"]
shopping_list_2.remove("bread")

print(shopping_list_2)

#Task 3: Add a function that prints out the entire list in a formatted way.

print(f"I am going to the store and buying:{shopping_list_2}")



