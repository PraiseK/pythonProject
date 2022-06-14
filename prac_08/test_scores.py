TESTS = 4


def main():
    total = 0
    scores = []
    for score in range(1, TESTS + 1):
        score = float(input(f"Score {score}: "))
        scores.append(score)
        total += score
    for score in scores:
        grade = determine_grade(score)
        print(f"Score was {score:.1f}, which is {grade}")
    average_score = calculate_average(total)
    print(f"The average score was {average_score}")
    trend = determine_trend(average_score, scores)
    print(f"The trend is {trend}")


def determine_grade(score):
    if score < 50:
        return "N"
    elif score < 65:
        return "P"
    elif score < 75:
        return "C"
    elif score < 85:
        return "D"
    return "HD"


def calculate_average(total):
    return total / TESTS


def determine_trend(average_score, scores):
    if scores[-1] > average_score:
        return "positive"
    else:
        return "not positive"


main()
