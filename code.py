# Imported packages
import operator
import random

operations_lookup = {'+': operator.add, '-': operator.sub, '*': operator.mul}
levels_lookup = {'1': 'simple operations with numbers 2-9',
                 '2': 'integral squares of 11-29'}
operations = ['+', '-', '*']
nums_for_diff_lvl_1 = range(2, 10)
nums_for_diff_lvl_2 = range(11, 30)
questions = 0
num_right_answers = 0


# Helper functions
def get_diff_lvl_from_user() -> str:
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

    return diff_lvl


def check_user_input() -> int:
    while True:
        try:
            user_input = int(input())
        except ValueError:
            print('Incorrect format.')
        else:
            break

    return user_input


def question_for_diff_lvl_1() -> tuple[str, int]:
    # Create the question
    first_num = random.choice(nums_for_diff_lvl_1)
    mid_op = random.choice(operations)
    second_num = random.choice(nums_for_diff_lvl_1)

    question = str(first_num) + ' ' + str(mid_op) + ' ' + str(second_num)
    correct_answer = operations_lookup[mid_op](first_num, second_num)

    return question, correct_answer


def question_for_diff_lvl_2() -> tuple[int, int]:
    # Choose a random number between 11 - 29, inclusive
    chosen_number = random.choice(nums_for_diff_lvl_2)
    correct_answer = chosen_number ** 2

    return chosen_number, correct_answer


# Determine the difficulty level the user would like to perform
diff_lvl = get_diff_lvl_from_user()

# Give the quiz to the user, depending on the chosen difficulty level
while questions < 5:

    if diff_lvl == '1':
        # Create the question and determine the <correct_answer>
        question, correct_answer = question_for_diff_lvl_1()

    else:  # <diff_lvl> == '2'
        # Create the question and determine the <correct_answer>
        question, correct_answer = question_for_diff_lvl_2()

    # Present <question> to the user
    print(question)

    # Take user input and check if correct
    user_input = check_user_input()

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
    file.write(f'{name}: {num_right_answers}/5 in level {diff_lvl} \
({levels_lookup[diff_lvl]}).\n')
    print('The results are saved in "results.txt".')
