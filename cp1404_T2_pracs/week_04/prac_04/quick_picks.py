import random

NUMBERS_PER_LINE = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

total_picks = int(input("Total quick picks(should be equal to or greater than 0): "))
for j in range(total_picks):
    solution_quick_picks = []

    for i in range(NUMBERS_PER_LINE):
        pick = random.randint(MIN_NUMBER, MAX_NUMBER)
        while pick in solution_quick_picks:
            pick = random.randint(MIN_NUMBER, MAX_NUMBER)
        solution_quick_picks.append(pick)
    solution_quick_picks.sort()
    print(" ".join("{:2}".format(pick) for pick in solution_quick_picks))

