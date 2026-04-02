""""A simple command-line mortgage/loan calculator program"""

def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        return float(number_str) <= 0
    except ValueError:
        return True
    
def invalid_number_APR(number_str):
    try:
        return float(number_str) < 0
    except ValueError:
        return True

prompt("Welcome to Mortgage Calculator")

while True:
    prompt("What's the loan amount?\nPlease use the following format: 50000 for $50,000")
    loan_amount = input()

    while invalid_number(loan_amount):
        prompt('Please enter a positive number')
        loan_amount = input()

    prompt('What is the Anual Percentage Rate?\nPlease use the following format: 5 for 5%.')
    APR = input()

    while invalid_number_APR(APR):
        prompt("Please enter '0' or a positive number")
        APR = input()

    prompt('What is the loan duration? Please enter the amount in years.')
    loan_duration = input()

    while invalid_number(loan_duration):
        prompt('Please enter a positive number')
        loan_duration = input()

    monthly_interest_rate = (float(APR)/100) / 12
    loan_duration_months = float(loan_duration) * 12
    loan_amount = float(loan_amount)

    if monthly_interest_rate == 0:
        monthly_payment = loan_amount / loan_duration_months
    else:
        monthly_payment = loan_amount * (
            monthly_interest_rate /
            (1 - (1 + monthly_interest_rate) ** (-loan_duration_months))
        )

    prompt(f'Your monthly payment is: ${monthly_payment:.2f}\n'
           f'Loan Details:\n- Loan Amount: ${loan_amount}\n- Interest Rate: {APR}%\n- Loan Duration: {loan_duration} years'
           )

    prompt('Would you like to perform another calculation (y/n)?')
    
    while True:
        answer = input().lower()
    
        if answer == 'y':
            break
        elif answer == 'n':
            prompt('Thank you for using Mortgage Loan Calculator!')
            exit()
        else:
            prompt("Invalid input. Would you like to perform another calculation? Please enter 'y' or 'n'.")
