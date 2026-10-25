from pathlib import Path

import numpy as np
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "students.csv"

ID_COLUMNS = ["student_id", "name", "department", "attendance"]
SUBJECT_COLUMNS = ["python", "mathematics", "database"]
SUBJECT_PASS_MARK = 40
OVERALL_PASS_AVERAGE = 50
ATTENDANCE_THRESHOLD = 75


def load_students(csv_path=DATA_FILE):
    """Load student records and validate required fields and marks."""
    df = pd.read_csv(csv_path)
    required = ID_COLUMNS + SUBJECT_COLUMNS
    missing = [column for column in required if column not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")

    if df["student_id"].duplicated().any():
        raise ValueError("Student IDs must be unique.")

    for column in SUBJECT_COLUMNS + ["attendance"]:
        df[column] = pd.to_numeric(df[column], errors="coerce")
        if df[column].isna().any():
            raise ValueError(f"Column '{column}' contains missing or non-numeric values.")
        if not df[column].between(0, 100).all():
            raise ValueError(f"Values in '{column}' must be between 0 and 100.")

    if df[["student_id", "name", "department"]].isna().any().any():
        raise ValueError("Student ID, name, and department cannot be empty.")

    return df


def assign_grade(average):
    """Assign a grade using the project's documented percentage bands."""
    if average >= 90:
        return "A+"
    if average >= 80:
        return "A"
    if average >= 70:
        return "B"
    if average >= 60:
        return "C"
    if average >= 50:
        return "D"
    return "F"


def analyze_students(df):
    """Return a copy with totals, averages, grades, results, and attendance flags."""
    result = df.copy()
    marks = result[SUBJECT_COLUMNS].to_numpy(dtype=float)
    result["total"] = np.sum(marks, axis=1)
    result["average"] = np.round(np.mean(marks, axis=1), 2)
    result["grade"] = result["average"].apply(assign_grade)
    passed_every_subject = (marks >= SUBJECT_PASS_MARK).all(axis=1)
    passed_average = result["average"] >= OVERALL_PASS_AVERAGE
    result["result"] = np.where(passed_every_subject & passed_average, "Pass", "Fail")
    result["attendance_status"] = np.where(
        result["attendance"] >= ATTENDANCE_THRESHOLD, "Good", "Low"
    )
    return result


def get_summary(analyzed_df):
    """Build summary values used by the dashboard."""
    subject_averages = analyzed_df[SUBJECT_COLUMNS].mean().round(2).to_dict()
    pass_count = int((analyzed_df["result"] == "Pass").sum())
    student_count = int(len(analyzed_df))
    return {
        "student_count": student_count,
        "class_average": round(float(analyzed_df["average"].mean()), 2) if student_count else 0,
        "pass_count": pass_count,
        "fail_count": student_count - pass_count,
        "pass_rate": round(pass_count / student_count * 100, 1) if student_count else 0,
        "highest_average": round(float(analyzed_df["average"].max()), 2) if student_count else 0,
        "lowest_average": round(float(analyzed_df["average"].min()), 2) if student_count else 0,
        "low_attendance_count": int((analyzed_df["attendance"] < ATTENDANCE_THRESHOLD).sum()),
        "subject_averages": subject_averages,
        "top_students": analyzed_df.sort_values(
            ["average", "name"], ascending=[False, True]
        ).head(5).to_dict(orient="records"),
        "grade_counts": analyzed_df["grade"].value_counts().reindex(
            ["A+", "A", "B", "C", "D", "F"], fill_value=0
        ).to_dict(),
    }
