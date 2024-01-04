student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for key in student_scores:
    grade = student_scores[key]
    if grade >= 91 and grade <= 100:
        student_grades[key] = "Outstanding"
    elif grade >= 81 and grade < 90:
        student_grades[key] = "Exceeds Expectations"
    elif grade >= 71 and grade < 80:
        student_grades[key] = "Acceptable"
    elif grade <= 70:
        student_grades[key] = "Fail"

print(student_grades)