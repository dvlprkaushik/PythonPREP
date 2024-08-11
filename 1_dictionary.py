student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 90,
    "Eve": 88
}

print(type(student_marks))
print(student_marks["Bob"])
print(student_marks)
print(student_marks.keys())
print(student_marks.values())
student_marks.update({"Charlie": 56})
print(student_marks)
print(student_marks.get("Kaushik")) #none
print(student_marks["Kaushik"]) #error
