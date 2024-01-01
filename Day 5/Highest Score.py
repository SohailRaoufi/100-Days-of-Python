student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
high = student_scores[0]
for score in student_scores:
    if score > high:
        high = score

print(high)