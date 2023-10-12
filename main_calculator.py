# Git link https://github.com/iHuGi/modulos_ExerciciosClass5.git

from calculator import calc_all

while True:
    try:
        number1 = float(input("Insert the first number: "))
        break
    except ValueError:
        print("Only numbers are accepted!")

while True:
    try:
        number2 = float(input("Insert the second number: "))
        break
    except ValueError:
        print("Only numbers are accepted!")

# List with valid operations
valid_operations = ['add', 'subtract', 'multiply', 'divide']

while True:
    operation = input("Select the type of operation (add, subtract, multiply, divide): ").lower()
    if operation in valid_operations:
        break
    else:
        print("Invalid operation. Please select a valid operation.")

# Call the function from our module
result = calc_all(number1, number2, operation)
print(f"Result: {result}")


