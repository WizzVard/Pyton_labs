bills = {
    1: "Volodymyr Velikiy",
    2: "Yaroslav Mudry",
    5: "Bogdan Hmelnitskiy",
    10: "Ivan Mazepa",
    20: "Ivan Franko",
    50: "Mihailo Grushevskiy",
    100: "Taras Shevchenko",
    200: "Lesia Ukrainka",
    500: "Grigoriy Skovoroda",
    1000: "Volodimir Vernadskiy"
}


def get_banknote_info(nominal):
    if nominal in bills:
        person = bills[nominal]
        return f"Banknote denomination: {nominal} uan.\nPerson on the banknote: {person}"
    else:
        return "There is no such a banknote."


if __name__ == '__main__':
    nominal = int(input("Enter the banknote denomination: "))
    result = get_banknote_info(nominal)
    print(result)