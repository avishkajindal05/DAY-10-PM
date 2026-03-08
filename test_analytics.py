from student_analytics import *


students = [
    create_student('Amit', 'R001', math=85, python=92, ml=78),
    create_student('Priya', 'R002', math=95, python=88, ml=91),
    create_student('Rahul', 'R003', math=60, python=70, ml=65),
]


# -----------------------
# create_student tests
# -----------------------

s = create_student("Test", "R100", math=90)
assert s["name"] == "Test"

assert s["marks"]["math"] == 90

try:
    create_student("", "R1")
except ValueError:
    assert True


# -----------------------
# calculate_gpa tests
# -----------------------

assert calculate_gpa(85, 92, 78) == 8.5

assert calculate_gpa(100, 100, 100) == 10.0

assert calculate_gpa(50, 60, scale=4) == 2.2


# -----------------------
# get_top_performers tests
# -----------------------

top = get_top_performers(students, n=1)
assert top[0]["name"] == "Priya"

top_python = get_top_performers(students, n=1, subject="python")
assert top_python[0]["name"] == "Amit"

assert len(get_top_performers([], 3)) == 0


# -----------------------
# generate_report tests
# -----------------------

report = generate_report(students[0])
assert "Amit" in report

report_verbose = generate_report(students[0], verbose=True)
assert "Marks" in report_verbose

report_no_grade = generate_report(students[0], include_grade=False)
assert "Grade" not in report_no_grade


# -----------------------
# classify_students tests
# -----------------------

classes = classify_students(students)

assert isinstance(classes, dict)

assert "A" in classes

assert any(s["name"] == "Priya" for s in classes["A"])

assert any(s["name"] == "Rahul" for s in classes["C"])


print("All tests passed!")

