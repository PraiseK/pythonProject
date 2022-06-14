def main():
    # height = float(input("Height (m): "))
    # weight = float(input("Weight (kg): "))
    age = get_valid_number("Age: ", 0, 120)
    print(age)
    height = get_valid_number("Height (m): ", 0, 3)
    print(height)
    weight = get_valid_number("Weight (kg): ", 0, 300)
    print(weight)
    bmi = calculate_bmi(height, weight)
    category = determine_weight_category(bmi)
    print(f"This BMI is {bmi:.1f}, which is considered {category}")


def get_valid_number(prompt, low, high):
    number = float(input(prompt))
    while number < low or number > high:
        print("Invalid input")
        number = float(input(prompt))
    return number


def rum_tests():
    bmi = calculate_bmi(2, 60)
    print(bmi)
    bmi = calculate_bmi(1.5, 100)
    print(bmi)
    print(determine_weight_category(16.5))
    print(determine_weight_category(25))


def calculate_bmi(height, weight):
    return weight / (height ** 2)


def determine_weight_category(bmi):
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "normal"
    else:
        return "obese"


# rum_tests()
main()
