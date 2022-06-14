"""2. Parity"""


def main():
    number = get_valid_number("Number: ", 1, 100)
    parity = calculate_parity(number)
    print(f"Parity of {number} is {parity:.0f} ")


def get_valid_number(prompt, low, high):
    number = float(input(prompt))
    while number < low or number > high:
        print("Invalid input")
        number = float(input(prompt))
    return number


def calculate_parity(number):
    return number % 2


def tests():
    parity = calculate_parity(4)
    print(f"Parity of 4 should be 0: {parity}")  # This should be 0
    parity = calculate_parity(41)
    print(f"Parity of 41 should be 1: {parity}")  # This should be 1


# tests()
main()