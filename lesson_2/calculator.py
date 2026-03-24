""""A simple command-line calculator program"""

# To Do list to code a calculator:
# 1. Ask the user for the first number.
# 2. Ask the user for the second number.
# 3. Ask the user for an operation to perform.
# 4. Perform the operation on the two numbers.
# 5. Print the result to the terminal.

# Defining prompt to differentiate user input from terminal output.
def prompt(message):
    print(f'==> {message}')

# Definiting invalid_number to loop back to question without having an error.
def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True
    return False

prompt('Welcome to Calculator!')                        # welcome message

prompt("What's the first number?")                      # asking user for first number
number1 = input()

while invalid_number(number1):
    prompt('That number is not valid, please re-enter the first number.')
    number1 = input()

prompt("What's the second number?")                     # asking user for second number
number2 = input()

while invalid_number(number2):
    prompt('That number is not valid, please re-enter the second number.')
    number2 = input()

prompt('What operation would you like to perform?\n'   # asking user for operation
      '1) Add 2) Subtract 3) Multiply 4) Divide')
operation = input()

while operation not in ['1', '2', '3', '4']:
    prompt('That operation is not valid. Please choose between 1, 2, 3, or 4.')
    operation = input()

match operation:
    case '1':                                          # '1' represents addition
        output = int(number1) + int(number2)
    case '2':                                          # '2' represents subtraction
        output = int(number1) - int(number2)
    case '3':                                          # '3' represents multiplication
        output = int(number1) * int(number2)
    case '4':                                          # '4' represents division
        output = int(number1) / int(number2)

prompt(f'The result is {output}')                      # this command prints the final result
