# define the functions
def calculator(num1, num2, operator):
    # + operater does addition
    if operator == '+':
        return  num1 + num2
    # - operator does subtraction
    elif operator == '-':
        return num1 - num2
    # * does multiplication
    elif operator == '*':
        return num1 * num2
    # / operator does division
    elif operator == '/':
        # we will check if num 2 is 0
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Divison by zero is invalid."
        # % modulus operator
    elif operator == '%':
        return num1 % num2
    else:
        return 'Invalid operator'   

try:
    # promot user to enter numbers and operator
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: ')) 
    operator = input('Enter operator (+, -, *, /, %): ')  

    result = calculator(num1, num2, operator)
   # print the output 
    print(result)
except ValueError:
    print('Error: Invalid input')    