import random
import csv

student_id = input('Enter your name or ID: ')

def problem_generator():
    y = random.randint(1, 10)
    x = random.randint(1, 10)
    z = y // x
    rem = y % x
    return f'{y} divided by {x}', (z, rem)

def classify_error(student_guess, answer):
    student_q, student_r = student_guess
    answer_q, answer_r = answer
    if student_q == answer_q and student_r == answer_r:
        return 'correct'
    elif student_q == answer_q and student_r != answer_r:
        return 'remainder_error'
    elif student_q != answer_q and student_r == answer_r:
        return 'quotient_error'
    else:
        return 'both_wrong'

score = 0

for i in range(1, 6):
    x = problem_generator()
    question, answer = x
    print(question)

    CD = input("Enter quotient: ")
    CD1 = int(CD)

    remainder = input("Enter remainder: ")
    rem1 = int(remainder)

    student_guess = (CD1, rem1)

    result = classify_error(student_guess, answer)

    with open("data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([student_id, question, answer, student_guess, result])
    print(question, answer, student_guess, result)

    if result == 'correct':
        score += 1
    else:
        pass

print(f'The score is {score} out of 5')