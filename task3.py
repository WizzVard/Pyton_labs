import math

print("Introduction to programming: Task 3")
print("Kustov Vadim")


def validate_input(b):
    while True:
        try:
            x = float(input("Enter x: "))
            if x > b:
                return x
            else:
                print("Invalid input. Please enter a number greater than", b)
        except ValueError:
            print("Invalid input.")


def func(x, c, b):
    y = (2 * x - c) / math.sqrt(x - b) + abs(x - c)
    return y


b = int(input("Enter b: "))
c = int(input("Enter c: "))
x = validate_input(b)
y = func(x, c, b)
print("Result:", round(y, 4))