# Cti-110
# Age Classifier
# Ryan Dumas
# 6/21/2018

# This is a program to classify a persons age
# Give the user a prompt

choice = "y"
while choice == "y":

# Get the age from the user

    age = int(input("Please enter the age from 0 to 100: "))

    if age <= 1:
        print("The individual is an infant.")
        print("The individual with an age of,",age,"is an infant.")
    elif age > 1 and age < 13:
        print("The individual is a child.")
        print("The individual with an age of,",age,"is an child.")
    elif age >= 13 and age < 20:
        print("The individual is a teenager.")
        print("The individual with an age of,",age,"is an teenager.")
    elif age >= 20 and age <= 100:
        print("The individual is an adult.")
        print("The individual with an age of,",age,"is an adult.")
    else:
        print("Invalid input, please try again.")
    choice = input("Would you like to check another age? Enter y for yes or n for no: ")
print("Goodbye")

    
        
        
        
    
