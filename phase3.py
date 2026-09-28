import random
import csv

student_id = input('Enter your name or ID: ')
mastery_totalRem = 0
mastery_totalQuotient = 0
mastery_Rem = 0
mastery_Quotient = 0
threshold = 2/3

# totals represented how many remainder
# or quotient parts the student got right

def problem_generator():
    y = random.randint(1, 10)
    x = random.randint(1, 10)
    z = y // x
    rem = y % x
    return f'{y} divided by {x}', (z, rem), (x,y)

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

def problem_generator_adaptive_case1():
    y = random.randint(1, 10)
    x = random.randint(1, 5)
    z = y // x
    rem = y % x
    return f'{y} divided by {x}', (z, rem), (x,y)

def problem_generator_adaptive_case2and3():
    y = random.randint(1, 5)
    x = random.randint(1, 5)
    z = y // x
    rem = y % x
    return f'{y} divided by {x}', (z, rem), (x,y)

for i in range(1, 6):
    if i == 1:
        x = problem_generator()
    elif (mastery_Quotient < threshold and mastery_Rem >= threshold):
        x = problem_generator_adaptive_case1()
    elif mastery_Rem >= threshold and mastery_Quotient >= threshold:
        x = problem_generator()
    elif mastery_Quotient < threshold and mastery_Rem < threshold:
        x = problem_generator_adaptive_case2and3()
    else:
        x = problem_generator_adaptive_case2and3()
    question, answer, original_numbers = x[0], x[1], x[2]
    quotient = answer[0]
    remainder_answer = answer[1]
    divisor = original_numbers[0]
    dividend = original_numbers[1]
    print(question)

    CD = input("Enter quotient: ")
    CD1 = int(CD)

    remainder = input("Enter remainder: ")
    rem1 = int(remainder)

    student_guess = (CD1, rem1)

    result = classify_error(student_guess, answer)

    if result == 'correct':
        mastery_totalRem+=1
        mastery_totalQuotient+=1
    elif result == 'remainder_error':
        mastery_totalQuotient+=1
        input(f"What's the closest you can get to {dividend} via multiples of {divisor}? ")
        input(f"What's {divisor} times {quotient}? ")
        remainder_correction = input(f'Whats {dividend} minus {divisor} times {quotient}? ')
        remainder_correction = int(remainder_correction)
        if remainder_correction == dividend - divisor*quotient:
            mastery_totalRem+=0.5
    elif result == 'quotient_error':
        mastery_totalRem+=1
        quotient_correction = input(f"What is {divisor} times {quotient}? ")
        quotient_correction = int(quotient_correction)
        if quotient_correction == dividend:
            mastery_totalQuotient += 0.5
    else:
        input(f"What's the closest you can get to {dividend} via multiples of {divisor}? ")
        input(f"What's {divisor} times {quotient}? ")
        remainder_correction = input(f'Whats {dividend} minus {divisor} times {quotient}? ')
        remainder_correction = int(remainder_correction)
        if remainder_correction == dividend - divisor * quotient:
            mastery_totalRem += 0.5
        quotient_correction = input(f"What is {divisor} times {quotient}? ")
        quotient_correction = int(quotient_correction)
        if quotient_correction == dividend:
            mastery_totalQuotient += 0.5

    mastery_Rem = mastery_totalRem / i
    mastery_Quotient = mastery_totalQuotient / i

    with open("data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([student_id, question, answer, student_guess, result, mastery_Rem, mastery_Quotient])
    print(question, answer, student_guess, result, mastery_Rem, mastery_Quotient)

