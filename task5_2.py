print("Introduction to programming: Task 3")
print("Kustov Vadim")


def validate_input():
    while True:
        try:
            return float(input("Enter a number: "))
        except ValueError:
            print("Invalid input")


def count_digits(n):
    if n == 0:  # якщо число одне
        return 1

    n = abs(n)  # якщо число від'ємне
    count = 0
    while n:
        count += 1
        n //= 10  # видаляємо останню цифру рядка
    return count


n = validate_input()
digit_count = count_digits(n)
print("Number of digits in the number:", digit_count)
