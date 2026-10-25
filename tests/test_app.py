import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from app import app


class RouteTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_main_pages_load(self):
        for url in ["/", "/students", "/students/STU001", "/download"]:
            self.assertEqual(self.client.get(url).status_code, 200, url)

    def test_unknown_student_returns_404(self):
        self.assertEqual(self.client.get("/students/NOPE").status_code, 404)

    def test_regex_characters_in_search_do_not_crash(self):
        for q in ["(", "[", "*", "a.b"]:
            self.assertEqual(self.client.get("/students", query_string={"q": q}).status_code, 200, q)

    def test_search_actually_filters(self):
        html = self.client.get("/students", query_string={"q": "Aarav"}).get_data(as_text=True)
        self.assertIn("Aarav Singh", html)
        self.assertNotIn("Diya Mishra", html)


if __name__ == "__main__":
    unittest.main()