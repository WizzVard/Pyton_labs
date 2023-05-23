from utils import validate_input


def calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == 'pow':
        return pow(a, b)
    elif operation == '/':
        return a / b if b != 0 else "Error: Division by zero!"
    elif operation == 'mod':
        return a % b if b != 0 else "Error: Division by zero!"
    elif operation == 'div':
        return a // b if b != 0 else "Error: Division by zero!"
    else:
        return 'Invalid operation'


if __name__ == '__main__':
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operation(+, -, /, *, mod, pow, div): ")
    print(f'Result: {calculator(a, b, op)}')