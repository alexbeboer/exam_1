#My teacher needs a program to switch her number grades into letter grades

num_grade = input('what is your grade?')
#Receive the users input which is a number
num_grade = float(num_grade)
# change from a number to a character
def grade(letter_g):
    if num_grade > 90:
        return ('Thats an A')
    elif num_grade > 80:
        return ('Thats a B')
    elif num_grade > 70:
        return('Thats a C')
    elif num_grade < 70:
        return('FAIL')
print(grade(num_grade))
