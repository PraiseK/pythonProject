#
import random


def main():
    numbers = int(input("How many random numbers: "))
    max_number = int(input("Maximum number: "))
    random_numbers = []
    while len(random_numbers) != numbers:
        values = random.randint(0, max_number)
        random_numbers.append(values)
    print(f"The numbers are: {random_numbers}")
    print("The minimum number is 0")
    print(f"The maximum number is {max_number}")
    print(f"A randomly chosen number is {values}")
    random_numbers.reverse()
    print("The numbers reversed are", random_numbers)
    random_numbers.sort()
    print("The numbers sorted are", random_numbers)

main()
