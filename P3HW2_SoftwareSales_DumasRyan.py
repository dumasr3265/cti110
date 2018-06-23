# Cti-110
# Software Sales
# Ryan Dumas
# 6/22/2018

# This is a program that calculates the total of a purchase with different discount rates
# Give the user a prompt


choice = "y"
while choice == "y":

#Get the quantity being purchased by the user

    quantity = int(input("How many packages are you purchasing today? "))

    if quantity >= 1 and quantity < 10:
        print("Your purchase does not qualify for a discount")
        total = quantity * 99
        print("The total of your purchase is $",format(total,',.2f'))

    elif quantity >= 10 and quantity < 20:
        print("Your purchase qualifies for a 10% discount")
        discount1 = quantity * 99 * .10
        total1 = quantity * 99 - discount1
        print("The discount saved you $",format(discount1,',.2f'))
        print("The total cost of your purchase with the discount is $",format(total1,',.2f'))
        

    elif quantity >= 20 and quantity < 50:
        print("Your purchase qualifies for a 20% discount")
        discount2 = quantity * 99 * .20
        total2 = quantity *99 - discount2
        print("The discount saved you $",format(discount2,',.2f'))
        print("The total cost of your purchase with the discount is $",format(total2,',.2f'))

    elif quantity >= 50 and quantity < 100:
        print("Your purchase qualifies for a 30% discount")
        discount3 = quantity * 99 * .30
        total3 = quantity * 99 - discount3
        print("The discount saved you $",format(discount3,',.2f'))
        print("The total cost of your purchase with the discount is $",format(total3,',.2f'))

    elif quantity >= 100:
        print("Your purchase qualifies for a 40% discount")
        discount4 = quantity * 99 * .40
        total4 = quantity * 99 - discount4
        print("The discount saved you $",format(discount4,',.2f'))
        print("The total cost of your purchase with the discount is $",format(total4,',.2f')) 
    else:
        print("Invalid input. Please try again.")
    choice = input("Would you like to make another purchase today? Enter y for yes or n for no: ")
print("Thank you for your business. Goodbye")



    
        
        
        
    
              
              
              
              
        
    
