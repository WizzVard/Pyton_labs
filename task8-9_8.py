def calculator(a, b, operation):
    operations = {
        '+': lambda x, y: a + b,
        '-': lambda x, y: a - b,
        '*': lambda x, y: a * b,
        'pow': lambda x, y: pow(a, b),
        '/': lambda x, y: a / b if b != 0 else "Error: Division by zero!",
        'mod': lambda x, y: a % b if b != 0 else "Error: Division by zero!",
        'div': lambda x, y: a // b if b != 0 else "Error: Division by zero!"
    }
    calc = operations.get(operation)
    if calc:
        return f'Result: {calc(a, b)}'
    else:
        return 'Invalid operation'


if __name__ == '__main__':
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operation(+, -, /, *, mod, pow, div): ")
    print(calculator(a, b, op))