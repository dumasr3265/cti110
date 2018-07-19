# CTI-110 
# P4HW2 - Running Total  
# Ryan Dumas
# 7/01/2018

# This program will keep a running total of numbers until the user inputs a negative number



def main():
    
    total = 0
    amount = float(input("Please enter the first number, or a negative number to exit: "))

    while amount >= 0:
        total = total + amount
        amount = float(input("Please enter the next number, or a negative number to see your total: "))
    print("The sum of all your numbers is: ",format(total,',.2f'))

main()
