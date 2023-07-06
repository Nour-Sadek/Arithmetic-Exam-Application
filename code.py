# Imported packages
import operator
import random

operations_lookup = {'+': operator.add, '-': operator.sub, '*': operator.mul}
levels_lookup = {'1': 'simple operations with numbers 2-9',
                 '2': 'integral squares of 11-29'}
operations = ['+', '-', '*']
nums = [2, 3, 4, 5, 6, 7, 8, 9]
questions = 0
num_right_answers = 0

# Determine the difficulty level the user would like to perform
while True:
    print("""Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29
    """)
    diff_lvl = input()
    if diff_lvl != '1' and diff_lvl != '2':
        print('Incorrect format.')
    else:
        break

# Give the quiz to the user, depending on the chosen difficulty level
while questions < 5:
    if diff_lvl == '1':
        # Create the question
        first_num = random.choice(nums)
        mid_op = random.choice(operations)
        second_num = random.choice(nums)

        statement = str(first_num) + ' ' + str(mid_op) + ' ' + str(second_num)
        print(statement)

        # Take user input and check if correct
        while True:
            try:
                user_input = int(input())
            except ValueError:
                print('Incorrect format.')
            else:
                break

        # Determine the value of the string expression
        num_1 = ''
        num_2 = ''
        operation = None
        switch = 0

        for num in statement:
            if num != ' ':
                if num not in operations and switch == 0:
                    num_1 = num_1 + num
                elif num not in operations and switch == 1:
                    num_2 = num_2 + num
                else:
                    operation = num
            elif num == ' ' and operation is not None:
                switch = 1

        num_1 = int(num_1)
        num_2 = int(num_2)
        operation = operations_lookup[operation]

        correct_answer = operation(num_1, num_2)

        # Compare correct answer of string expression to <user_input>
        if user_input == correct_answer:
            print('Right!')
            num_right_answers += 1
        else:
            print('Wrong!')

        questions += 1

    else:  # <diff_lvl> == '2'
        # Create the number
        numbers = range(11, 30)
        number = random.choice(numbers)
        correct_answer = number ** 2

        print(number)

        # Take user input and check if correct
        while True:
            try:
                user_input = int(input())
            except ValueError:
                print('Incorrect format.')
            else:
                break

        # Compare correct answer of string expression to <user_input>
        if user_input == correct_answer:
            print('Right!')
            num_right_answers += 1
        else:
            print('Wrong!')

        questions += 1

# Asking the user if they want to save the results or not
print(f'Your mark is {num_right_answers}/5. Would you like to save the result? \
Enter yes or no.')
user_answer = input()

# If user says no or any other input, exit the program
if user_answer in ['yes', 'YES', 'y', 'Yes']:
    print('What is your name?')
    name = input()
    file = open('results.txt', 'a')
    file.write(
        f'{name}: {num_right_answers}/5 in level {diff_lvl} ({levels_lookup[diff_lvl]}).')
    print('The results are saved in "results.txt".')
