print("=== POCKET CGPA CALCULATOR ===")

num_courses = int(input("Enter number of courses: "))

total_units = 0
total_grade_points = 0

grade_point = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
    "E": 1,
    "F": 0
}

for i in range(num_courses):
    print(f"\nCourse {i+1}")

    course = input("Course Code: ")
    unit = int(input("Course Unit: "))
    grade = input("Grade (A-F): ").upper()

    while grade not in grade_point:
        print("Invalid grade!")
        grade = input("Grade (A-F): ").upper()

    point = grade_point[grade]
    total_units += unit
    total_grade_points += unit * point

gpa = total_grade_points / total_units

print("\n===== RESULT =====")
print("Total Units:", total_units)
print("Total Grade Points:", total_grade_points)
print("CGPA:", round(gpa, 2))

if gpa >= 4.50:
    print("Class: First Class")
elif gpa >= 3.50:
    print("Class: Second Class Upper")
elif gpa >= 2.40:
    print("Class: Second Class Lower")
elif gpa >= 1.50:
    print("Class: Third Class")
elif gpa >= 1.00:
    print("Class: Pass")
else:
    print("Class: Fail")
