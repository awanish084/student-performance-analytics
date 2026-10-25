import sys
import unittest
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from analytics import analyze_students, assign_grade, get_summary, load_students


class AnalyticsTests(unittest.TestCase):
    def test_grade_boundaries(self):
        self.assertEqual(assign_grade(95), "A+")
        self.assertEqual(assign_grade(80), "A")
        self.assertEqual(assign_grade(70), "B")
        self.assertEqual(assign_grade(60), "C")
        self.assertEqual(assign_grade(50), "D")
        self.assertEqual(assign_grade(49.99), "F")

    def test_dataset_has_at_least_15_records(self):
        self.assertGreaterEqual(len(load_students()), 15)

    def test_totals_average_and_pass_rule(self):
        sample = pd.DataFrame([{
            "student_id": "T001", "name": "Test Student", "department": "CSE",
            "python": 80, "mathematics": 70, "database": 90, "attendance": 80
        }])
        analyzed = analyze_students(sample).iloc[0]
        self.assertEqual(analyzed["total"], 240)
        self.assertEqual(analyzed["average"], 80)
        self.assertEqual(analyzed["grade"], "A")
        self.assertEqual(analyzed["result"], "Pass")

    def test_fails_if_any_subject_is_below_40(self):
        sample = pd.DataFrame([{
            "student_id": "T002", "name": "Fail Student", "department": "IT",
            "python": 90, "mathematics": 39, "database": 90, "attendance": 90
        }])
        analyzed = analyze_students(sample).iloc[0]
        self.assertEqual(analyzed["result"], "Fail")
    def test_fails_if_average_below_50_even_when_every_subject_is_40_plus(self):
        sample = pd.DataFrame([{
            "student_id": "T003", "name": "Borderline Student", "department": "CSE",
            "python": 45, "mathematics": 50, "database": 50, "attendance": 90
        }])  # average = 48.33, all subjects >= 40
        analyzed = analyze_students(sample).iloc[0]
        self.assertEqual(analyzed["grade"], "F")
        self.assertEqual(analyzed["result"], "Fail")

    def test_passes_at_exact_boundaries(self):
        sample = pd.DataFrame([{
            "student_id": "T004", "name": "Boundary Student", "department": "IT",
            "python": 40, "mathematics": 60, "database": 50, "attendance": 80
        }])  # lowest subject = 40, average = 50.00
        analyzed = analyze_students(sample).iloc[0]
        self.assertEqual(analyzed["average"], 50)
        self.assertEqual(analyzed["result"], "Pass")

    def test_no_student_has_pass_with_grade_f(self):
        data = analyze_students(load_students())
        self.assertFalse(((data["result"] == "Pass") & (data["grade"] == "F")).any())
    def test_summary_counts_all_students(self):
        data = analyze_students(load_students())
        summary = get_summary(data)
        self.assertEqual(summary["student_count"], 20)
        self.assertEqual(summary["pass_count"] + summary["fail_count"], 20)
        self.assertEqual(len(summary["top_students"]), 5)


if __name__ == "__main__":
    unittest.main()
