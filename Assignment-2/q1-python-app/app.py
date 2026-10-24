import os

APP_NAME = os.getenv("APP_NAME", "Student Marks Analyzer")
PASS_PERCENTAGE = float(os.getenv("PASS_PERCENTAGE", "40"))


def calculate_results(filename):
    with open(filename, "r", encoding="utf-8") as file:
        marks = [
            float(line.strip())
            for line in file
            if line.strip()
        ]

    if not marks:
        raise ValueError("The marks file contains no student marks.")

    if any(mark < 0 or mark > 100 for mark in marks):
        raise ValueError("Every mark must be between 0 and 100.")

    total_students = len(marks)
    average = sum(marks) / total_students

    passed = sum(
        1 for mark in marks
        if mark >= PASS_PERCENTAGE
    )

    pass_percentage = (passed / total_students) * 100

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "F"

    return average, grade, pass_percentage, passed, total_students


if __name__ == "__main__":
    average, grade, pass_percentage, passed, total = (
        calculate_results("marks.txt")
    )

    print(f"Application: {APP_NAME}")
    print(f"Average marks: {average:.2f}")
    print(f"Grade: {grade}")
    print(f"Students passed: {passed}/{total}")
    print(f"Pass percentage: {pass_percentage:.2f}%")
