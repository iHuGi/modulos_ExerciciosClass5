
def calc_sum(num1, num2):
    return num1 + num2

def calc_divide(num1, num2):
    return num1 / num2

def calc_multiply(num1, num2):
    return num1 * num2

def calc_subtract(num1, num2):
    return num1 - num2

def calc_all(num1, num2, operation):
    if operation == 'add':
        return calc_sum(num1, num2)
    elif operation == 'divide':
        return calc_divide(num1, num2)
    elif operation == 'multiply':
        return calc_multiply(num1, num2)
    elif operation == 'subtract':
        return calc_subtract(num1, num2)
    else:
        return "Invalid!"

