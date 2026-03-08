from collections import defaultdict
from typing import Dict, List, Any


def create_student(name: str, roll: str, **marks: int) -> Dict[str, Any]:
    """
    Create a student record.

    Args:
        name: Student name.
        roll: Unique roll number.
        **marks: Subject marks as keyword arguments.

    Returns:
        A dictionary representing the student.

    Raises:
        ValueError: If name/roll empty or marks invalid.
    """

    if not name or not roll:
        raise ValueError("Name and roll cannot be empty")

    clean_marks = {}

    for subject, score in marks.items():
        if not isinstance(score, (int, float)):
            raise ValueError(f"Invalid mark for {subject}")
        if score < 0 or score > 100:
            raise ValueError(f"Marks must be between 0 and 100 for {subject}")

        clean_marks[subject] = int(score)

    return {
        "name": name,
        "roll": roll,
        "marks": clean_marks,
        "attendance": 0.0
    }


def calculate_gpa(*marks: float, scale: float = 10.0) -> float:
    """
    Calculate GPA using arbitrary number of marks.

    Args:
        *marks: Any number of marks.
        scale: GPA scale (default 10).

    Returns:
        GPA value.

    Raises:
        ValueError: If marks list empty.
    """

    if not marks:
        raise ValueError("At least one mark required")

    valid_marks = [m for m in marks if isinstance(m, (int, float))]

    if not valid_marks:
        raise ValueError("Invalid marks provided")

    avg = sum(valid_marks) / len(valid_marks)

    gpa = (avg / 100) * scale

    return round(gpa, 2)


def get_top_performers(
    students: List[Dict[str, Any]],
    n: int = 5,
    subject: str | None = None
) -> List[Dict[str, Any]]:
    """
    Return top N performing students.

    Args:
        students: List of student dictionaries.
        n: Number of top students to return.
        subject: Optional subject filter.

    Returns:
        List of top student records.
    """

    if not students:
        return []

    def avg_marks(student: Dict[str, Any]) -> float:
        marks = student.get("marks", {})
        if not marks:
            return 0
        return sum(marks.values()) / len(marks)

    if subject:

        ranked = sorted(
            students,
            key=lambda s: s.get("marks", {}).get(subject, 0),
            reverse=True
        )

    else:

        ranked = sorted(
            students,
            key=avg_marks,
            reverse=True
        )

    return ranked[:n]


def generate_report(student: Dict[str, Any], **options) -> str:
    """
    Generate formatted student performance report.

    Args:
        student: Student record.
        **options:
            include_rank (bool)
            include_grade (bool)
            verbose (bool)

    Returns:
        Formatted report string.
    """

    include_rank = options.get("include_rank", True)
    include_grade = options.get("include_grade", True)
    verbose = options.get("verbose", False)

    name = student.get("name", "Unknown")
    roll = student.get("roll", "N/A")
    marks = student.get("marks", {})

    if not marks:
        avg = 0
    else:
        avg = sum(marks.values()) / len(marks)

    report = f"Student: {name} ({roll})\n"
    report += f"Average: {round(avg,2)}\n"

    if verbose:
        report += f"Marks: {marks}\n"

    if include_grade:

        if avg >= 90:
            grade = "A"
        elif avg >= 75:
            grade = "B"
        elif avg >= 60:
            grade = "C"
        else:
            grade = "D"

        report += f"Grade: {grade}\n"

    if include_rank:
        report += "Rank: N/A\n"

    return report.strip()


def classify_students(students: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    """
    Classify students into grade categories.

    Args:
        students: List of student records.

    Returns:
        Dictionary with grade buckets.
    """

    categories = defaultdict(list)

    if not students:
        return {"A": [], "B": [], "C": [], "D": []}

    for student in students:

        marks = student.get("marks", {})

        if not marks:
            avg = 0
        else:
            avg = sum(marks.values()) / len(marks)

        if avg >= 90:
            categories["A"].append(student)

        elif avg >= 75:
            categories["B"].append(student)

        elif avg >= 60:
            categories["C"].append(student)

        else:
            categories["D"].append(student)

    for grade in ["A", "B", "C", "D"]:
        categories.setdefault(grade, [])

    return dict(categories)