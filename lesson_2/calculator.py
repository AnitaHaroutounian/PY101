""""A simple command-line calculator program"""

# To Do list to code a calculator:
# 1. Ask the user for the first number.
# 2. Ask the user for the second number.
# 3. Ask the user for an operation to perform.
# 4. Perform the operation on the two numbers.
# 5. Print the result to the terminal.

import json

LANGUAGE = 'en'

YES_CHARACTERS = {
    'en': 'y',
    'fr': 'o'
}[LANGUAGE]

# Defining prompt to differentiate user input from terminal output.
def prompt(key):
    message = messages(key, LANGUAGE)
    print(f'==> {message}')

# Definiting invalid_number to loop back to question without having an error.
def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False

def messages(message, lang=LANGUAGE):
    return MESSAGES[lang][message]

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

print(messages('welcome'))                                 # welcome message

while True:
    prompt('number_prompt_1')                              # asking user for first number
    number1 = input()

    while invalid_number(number1):
        prompt('invalid_number')
        number1 = input()

    prompt('number_prompt_2')                              # asking user for second number
    number2 = input()

    while invalid_number(number2):
        prompt('invalid_number')
        number2 = input()

    prompt('operation_prompt')                             # asking user for operation
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt('invalid_operation')
        operation = input()

    match operation:
        case '1':                                          # '1' represents addition
            output = float(number1) + float(number2)
        case '2':                                          # '2' represents subtraction
            output = float(number1) - float(number2)
        case '3':                                          # '3' represents multiplication
            output = float(number1) * float(number2)
        case '4':                                          # '4' represents division
            output = float(number1) / float(number2)

    prompt('result'.format(output=output))                 # this command prints the final result

    prompt('another_operation')
    answer = input()
    if answer and answer[0].lower() != YES_CHARACTERS:
        break
