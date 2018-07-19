# CTI-110 
# P5HW1 - Test Average and Grade
# Ryan Dumas
# 7/10/2018

# This program calculates the average and letter grade of 5 tests.





def main():
    grade1 = getGrade1()
    grade2 = getGrade2()
    grade3 = getGrade3()
    grade4 = getGrade4()
    grade5 = getGrade5()

    get_average = calc_average(grade1, grade2, grade3, grade4, grade5)
    final_letter = determine_grade(get_average)

    



def getGrade1():
    grade1 = float(input('Enter your first numeric grade: '))
    return grade1
def getGrade2():
    grade2 = float(input('Enter your second numeric grade: '))
    return grade2
def getGrade3():
    grade3 = float(input('Enter your third numeric grade: '))
    return grade3
def getGrade4():
    grade4 = float(input('Enter your fourth numeric grade: '))
    return grade4
def getGrade5():
    grade5 = float(input('Enter your fifth numeric grade: '))
    return grade5
    
def calc_average(grade1, grade2, grade3, grade4, grade5):
    total = grade1 + grade2 + grade3 + grade4 + grade5
    avg = total / 5
    return avg

def determine_grade(get_average):
    if get_average > 89 and get_average < 101:
        print("You made an A!")
        print("Your average is",get_average,"your letter grade is A!")
    elif get_average > 79 and get_average < 90:
        print("You made an B!")
        print("Your average is",get_average,"your letter grade is B!")
    elif get_average > 69 and get_average < 80:
        print("You made an C!")
        print("Your average is",get_average,"your letter grade is C!")
    elif get_average > 59 and get_average < 70:
        print("You made an D!")
        print("Your average is",get_average,"your letter grade D!")
    elif get_average >= 0 and get_average < 60:
        print("You made an F!")
        print("Your average is",get_average,"you failed and got an F!")
   

main()
