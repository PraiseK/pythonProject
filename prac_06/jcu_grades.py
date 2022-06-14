"""3. JCU Grades"""

import random


def main():
    scores = []
    score = float(input("Score: "))
    while score >= 0:
        grade = determine_grade(score)
        print(f"The score {score} is {grade}")
        score = float(input("Score: "))
        scores.append(score)

    number_of_scores = int(input("How many random scores: "))
    for i in range(1, number_of_scores + 1):

        grade = determine_grade(score)
        print(f"{score} = {grade}")
    average = sum(scores) / len(scores)
    print("The average score was", average)


def determine_grade(score):
    if score < 50:
        return "F"
    elif score < 65:
        return "P"
    elif score < 75:
        return "C"
    elif score < 85:
        return "D"
    return "HD"


main()

