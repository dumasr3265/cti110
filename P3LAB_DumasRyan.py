# CTI-110
# Letter Grade
# Ryan Dumas
# 6/24/2018

def main():
# This program takes a number grade and outputs a letter grade.

    choice = "y"
    while choice == "y":    

# system uses 10-point grading scale
# TO DO: define the rest of the scores
        A_score = 90 
        B_score = 80
        C_score = 70
        D_score = 60
        F_score = 59
        
    
# Get the numerical grade from the user
    
        score = int(input('Enter grade: '))

        if score >= A_score and score < 101:
            print('Your grade is: A')
        elif score >= B_score and score < A_score:
            print('Your grade is: B')
        elif score >= C_score and score < B_score:
            print('Your grade is: C')
        elif score >= D_score and score < C_score:
            print('Your grade is: D')
        elif score <= F_score and score < D_score:
            print('Your grade is: F')
        else:
            print('Invalid input. Try again')
        choice = input('Would you like to check another grade? Enter y for yes or n for no: ')
    print("Goodbye")
            
            


# program start
main()
