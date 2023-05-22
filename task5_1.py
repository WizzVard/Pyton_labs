import math

print("Introduction to programming: Task 3")
print("Kustov Vadim")


def calculate_series_sum(epsilon=0.0001):
    sum = 0
    value = 1  # значення ряду в даний момент
    n = 0
    while abs(value) >= epsilon:
        value = ((3 ** n) * math.factorial(n)) / math.factorial(3 * n)
        sum += value  # обчислення загальної суми ряду
        n += 1
    return round(sum, 4)


result = calculate_series_sum()
print("Value of the sum of the series is", result)
