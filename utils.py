def calculate_average(scores):
    return round(sum(scores) / len(scores), 2)

def calculate_total(scores):
    return sum(scores)

def assign_grade(average):
    if average >= 85:
        return 'A'
    elif average >= 75:
        return 'B'
    elif average >= 65:
        return 'C'
    elif average >= 50:
        return 'D'
    else:
        return 'F'
