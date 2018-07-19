# This program converts feet to inches
# 7/05/2018
# CTI-110 P5T2_FeetToInches 
# Ryan Dumas

inches_per_foot = 12


def main():
    feet = int(input("Enter a number of feet: "))
    if feet == 1:
        print(feet,'foot is equivalant to', feet_to_inches(feet), 'inches.')
    elif feet > 1:
        print(feet,'feet is equivalant to', feet_to_inches(feet), 'inches.')


def feet_to_inches(feet):
    return feet * inches_per_foot


    

main()
