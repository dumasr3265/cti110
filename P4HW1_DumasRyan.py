# CTI-110
# P4HW1- Distance Traveled
# Ryan Dumas
# 7/01/2018

# This program calculates the distance traveled and displays the distance for each hour

def main():

# Get input from user

    speed = int(input("What speed in mph are you travling? "))

    hours = int(input("How many hours have you been driving? "))
    print()

# Create title

    title = "Distance Traveled"
    y = "Hour"
    z = "Distance Traveled"
    print(title.center(30))
    print()
    print(y.rjust(0) + z.rjust(30))
    print("-"*35)

    for x in range( 1, hours + 1):
        distanceTraveled = speed * x
        
    
        print(x,'\t', '\t',distanceTraveled,)


main()
    
