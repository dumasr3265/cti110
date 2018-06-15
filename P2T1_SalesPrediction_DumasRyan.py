# CTI-110 
# P2T1 - Sales Prediction 
# Ryan Dumas
# 6/13/2018


#This is a program to caluculate the total profit off of a given projected annual sale amount



#get the totalSales amount from the user

totalSales = float(input("Give me the projected total annual sales amount: $" ))

                         

#get the annualProfit

annualProfit = totalSales * .23




#display the annualProfit

print("the annual profit calculated at 23% is $",format(annualProfit,',.2f'))
