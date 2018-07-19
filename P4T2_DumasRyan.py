# CTI-110 
# P4T2 - Bug Collector 
# Ryan Dumas
# 6/28/2018


def main():

# This program keeps a running total of bugs caught in a week
    print("This program will calculate how many bugs you have caught this week.")
    print()

# Initialize accumlator to zero
    total = 0

# Get the number of days worked by user

    num = 7

# Run for loop to get the total
    for x in range(1, num + 1):
        print("How many bugs did you catch on day ",x,"? : ",sep="",end="")
        bugs = int(input())
        total = total + bugs
    print("The total amount of bugs you caught this week is:",total,)


main()


