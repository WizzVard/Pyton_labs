def calculate_percentage(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    total_letters = sum(1 for char in text if char.isalpha())
    lowercase_letters = sum(1 for char in text if char.isalpha() and char.islower())
    uppercase_letters = sum(1 for char in text if char.isalpha() and char.isupper())

    lowercase_percentage = (lowercase_letters / total_letters) * 100 if total_letters > 0 else 0
    uppercase_percentage = (uppercase_letters / total_letters) * 100 if total_letters > 0 else 0

    return lowercase_percentage, uppercase_percentage


file_path = 'Monte_Cristo.txt'
lowercase_percentage, uppercase_percentage = calculate_percentage(file_path)

print(f"Percentage of small letters: {lowercase_percentage:.2f}%")
print(f"Percentage of capital letters: {uppercase_percentage:.2f}%")