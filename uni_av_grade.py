grades = {"Ana1": (9, 6), "Linalg1": (9, 6), "Foundations": (3, 5.5), "Info1": (6,6), 
"Ana2": (12, 6), "Linalg2": (9, 5), "Info2": (6,6)}

def average():
    global grades
    total_credits = 0
    total_grades = 0
    for info in grades.values():
        total_credits += info[0]
        total_grades += info[0] * info[1]
    return total_grades / total_credits

averagec = average()
print(averagec)