# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f

mode = input('Enter math operation (+,-,*,/, f for Celsius to Fahrenheit conversion): ')

# Convert user input from string to float
num1 = float(input('Enter first number: '))

# Use .lower() method to make user input lower case
if mode.lower() == 'f':
    print(f'{num1} degrees Celsius converts to {(num1*9)/5 + 32} degrees Fahrenheit')
else:
    num2 = float(input('Enter second number: '))

    if mode == '+':
        print(f'Answer is: {num1 + num2}')

    elif mode == '-':
        print(f'Answer is: {num1 - num2}')

    elif mode == '*':
        print(f'Answer is: {num1 * num2}')

    elif mode == '/':
        print(f'Answer is: {num1 / num2}')

    # Added else clause in case user types an invalid operation
    else:
        print('ERROR. That is not a valid operation.')
