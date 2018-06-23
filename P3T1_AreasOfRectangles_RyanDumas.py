# CTI=110
# P3T1-Areas of Rectangles
# Ryan Dumas
# 6/19/2018

#This is a program to determine which of two rectangles has a larger area
#Give the user a prompt

choice = "y"
while choice == "y":
    

#get the firstLength of the firstRectangle from the user
    firstLength = float(input("What is the length of the first rectangle?: " ))

#get the firstWidth of the firsRectangle from the user
    firstWidth = float(input("What is the width of the first rectangle?: " ))

#get the firstArea of the firstRectangle
    firstArea = firstLength * firstWidth



#get the secondLength of the secondRectangle from the user
    secondLength = float(input("What is the length of the second rectangle?: " ))

#get the secondWidth of the secondRectangle from the user
    secondWidth = float(input("What is the width of the second rectangle?: " ))

#get the secondArea of the secondRectangle
    secondArea = secondLength * secondWidth


    if firstArea > secondArea:
        print("The first rectangle has a greater area")
    elif firstArea < secondArea:
        print("The second rectangle has a greater area")
    elif firstArea == secondArea:
        print("The rectangles have the same area")
    choice = input("Would you like to compare more rectangles? Enter y for yes or n for no: ")
print("Goodbye")

        
    







