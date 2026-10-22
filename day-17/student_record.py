students = [
    {"name": "Aarav", "score": 85},
    {"name": "Diya", "score": 64},
    {"name": "Kabir", "score": 92},
    {"name": "Meera", "score": 70}
]

for student in students:
    if student["score"] >= 70:
        print(student["name"])