student_score = {
    "Harry": 81,
    "James": 79,
    "Krishna": 100,
    "Misha": 30
}

student_grades = {}
for students in student_score:
    if student_score[students] > 90:
        student_grades[students] = "outstanding"
    elif student_score[students] > 80:
        student_grades[students] = "exceeds Expectation"
    elif student_score[students] > 80:
        student_grades[students] = "acceptable"
    else:
        student_grades[students] = "fail"

print(student_grades)
