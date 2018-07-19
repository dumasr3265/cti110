# This program converts kilometers to miles
# 7/05/2018
# CTI-110 P5T1_KM_to_Miles 
# Ryan Dumas


def main():
    show_miles()

    


def show_miles():
    kilos = float(input("Enter your distance in kilometers: "))
    
    miles = kilos * 0.6214
    print("Your distance converted to miles is ",format(miles,',.2f'))




main()
