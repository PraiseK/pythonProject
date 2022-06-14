'''

Testing for funcions
'''


def celsius_to_fahrenheit(celsius):
    return celsius * 1.8 + 32.0
    '''Convert celsius to fahrenheit'''


def main():
    number = 5
    print(f'{number} ^ 2 = {square(number)}')
    f_degree = celsius_to_fahrenheit(21)
    # print(f'{f_degree:.1f}')


# def is_even(number):
#     return number % 2 == 0


def square(number):
    return number ** 2


# square()
main()
