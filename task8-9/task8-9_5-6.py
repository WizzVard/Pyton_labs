def count_days_in_month(month):
    months = {'January': 31, 'February': '28 or 29',
              'March': 31, 'April': 30, 'May': 31,
              'June': 30, 'July': 31, 'August': 31,
              'September': 30, 'October': 31,
              'November': 30, 'December': 31}
    return months.get(month, 'Invalid month')


def leap_year(year):
    return 'Leap year' if year % 4 == 0 and year % 100 != 0 else 'Ordinary year'


if __name__ == '__main__':
    month_name = input('Enter month name: ')
    print(f'In {month_name} - {count_days_in_month(month_name)} days')

    year = int(input('Enter year: '))
    print(leap_year(year))


