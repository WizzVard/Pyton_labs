print("Introduction to programming: Task 3")
print("Kustov Vadim")


def validate_input():
    while True:
        try:
            return float(input("Enter a number: "))
        except ValueError:
            print("Invalid input")


def validate_positive_number():
    while True:
        a = validate_input()
        if a > 0:
            return a
        else:
            print("Invalid input, please enter positive number.")


def heron(a, x, epsilon=0.0001):
    xn = x  # початкове наближене значення
    xn_1 = (1/2) * (xn + a / xn)
    while abs(xn_1 - xn) >= epsilon:
        # оновлення наближеного значення
        xn, xn_1 = xn_1, (1/2) * (xn_1 + a / xn_1)
    return round(xn_1, 4)


a = validate_positive_number()
x = validate_positive_number()
square_root = heron(a, x)
print("The square root of a is", square_root)
