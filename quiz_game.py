#Objective:
#The aim of this assignment is to create a quiz game that asks questions and checks answers.

#Task 1: Develop a list of questions and answers.

questions = ("What is the third planet in the solar system?", "How many sides does a pentagon have?", 
             "What did Cinderella lose when running from the prince?")
answers = ("Earth", "5", "Shoe")

#Task 2: Write a function that quizzes the user and takes their answers.

answer = input("In what city can you find the Eiffel Tower?")
if answer == "Paris" or "paris":
    print("That's right!")
else:
    print("Try again!")

answer = input("What animal is the king of the jungle?")
if answer == "lion" or "Lion":
    print("That's right!")
else:
    print("Try again!")

#Task 3: Score the quiz and give the user feedback on their performance.

answer = input("In what city can you find the Eiffel Tower?")
if answer == "Paris" or "paris":
    print(f"That's right!" + "You get 100%")



