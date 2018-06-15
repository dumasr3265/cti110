# CTI-110 
# P2HW2 - Tip Tax Total 
# Ryan Dumas
# 6/12/2018

#Write a program to calculate the total cost of a meal purchased at a restaurant

#get the foodCost from the user

foodCost = float(input("Give me the cost of the food: $" ))


#get the tipAmount

tipAmount = foodCost * .18

#display the tipAmount

print("the tip at 18% is $",format(tipAmount,',.2f'))


#get the salesTax

salesTax = foodCost * .07

#display the salesTax

print("the sales tax at 7% is $",format(salesTax,',.2f'))


#get the totalCost

totalCost = foodCost + tipAmount + salesTax

#display the totalCost

print("the total cost is $",format(totalCost,',.2f'))



