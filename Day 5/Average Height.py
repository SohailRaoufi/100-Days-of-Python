student_heights = [180, 124, 165, 173, 189, 169, 146]
sum = 0
len = 0
for student in student_heights:
    sum += student
    len += 1

avg_height = round(sum / len)
print(f"Average Student Heights in list is: {avg_height}.")
