student_marks = {
    "Aman": 85,
    "Riya": 92,
    "Kabir": 85
}

inverted = {}

for name, marks in student_marks.items():
    if marks not in inverted:
        inverted[marks] = [name]
    else:
        inverted[marks].append(name)

        print(inverted)