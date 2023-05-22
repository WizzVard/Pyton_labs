import math

print("Introduction to programming: Task 4")
print("Kustov Vadim")


def validate_input():
    while True:
        try:
            return float(input("Enter a number: "))
        except ValueError:
            print("Invalid input")


def find_max(c, d):
    step = 0.001
    max_value = -math.inf
    num_steps = int((d - c) / step) + 1  # Обчислюємо кількість кроків
    for i in range(num_steps):
        x = c + i * step  # Ітерування через відрізок
        y = math.sin(x*x)*x + math.cos(x)
        if y > max_value:  # Пошук максимального значення
            max_value = y
    return round(max_value, 3)


left_contour = validate_input()
right_contour = validate_input()
result = find_max(left_contour, right_contour)
print("Result:", result)