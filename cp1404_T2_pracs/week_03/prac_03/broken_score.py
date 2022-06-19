"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random


def main():
    score = float(input("Enter score: "))
    print(determine_grade(score))
    random_score = random.randint(0, 100)
    print(f'Random score is {random_score} and the result is {determine_grade(random_score)}')


def determine_grade(score):
    if score < 0 or score > 100:
        return "Invalid"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


main()
