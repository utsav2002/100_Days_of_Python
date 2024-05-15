import random

names = ["Utsav", "Esha", "Devraj", "Tanishka", "Maulish", "Anvitha", "Devansh", "Shreya"]
student_scores = {student:random.randint(0, 100) for student in names}

passed_students = {
    student:student_scores[student] for student in student_scores if (student_scores[student] > 40)
}

print(passed_students)
