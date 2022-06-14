"""1. Coffee Brew Ratio"""


def main():
    dose = get_valid_number("Dose (g): ", 1, 100)
    grams_of_yield = get_valid_number("Yield (g): ", 1, 100)
    ratio = calculate_ratio(grams_of_yield, dose)
    style = determine_coffee_style(ratio)
    print(f"1:{ratio} is considered {style}")


def get_valid_number(prompt, low, high):
    number = float(input(prompt))
    while number < low or number > high:
        print("Invalid input")
        number = float(input(prompt))
    return number


def calculate_ratio(grams_of_yield, dose):
    return grams_of_yield / dose


def determine_coffee_style(ratio):
    if ratio < 2:
        return "risetretto"
    elif ratio < 3:
        return "normale"
    else:
        return "lungo"


def check_coffee():
    style = determine_coffee_style(1)
    print(style)  # This should be ristretto
    style = determine_coffee_style(2)
    print(style)  # This should be normale
    style = determine_coffee_style(13.5)
    print(style)  # This should be lungo


# check_coffee()
main()
