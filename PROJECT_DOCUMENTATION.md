# Project Documentation: Student Performance Analytics System

## 1. Project Title and Student Details

**Project:** Student Performance Analytics System  
**Student Name:** Awanish Sharma  
**Course:** EWB Courses — Python with AI  
**Institution:** Veer Bahadur Singh Purvanchal University, Jaunpur, Uttar Pradesh  
**Submission Date:** 26 October 2026  
**GitHub Repository:** https://github.com/awanish084/student-performance-analytics

## 2. Objective

The objective is to build a Python-based application that processes student records and presents meaningful academic insights. It calculates total and average marks, assigns grades, identifies pass/fail outcomes, compares subject performance, identifies top performers, and flags attendance below a defined threshold.

## 3. Technologies Used

- Python for program logic and functions
- Flask for web routes and dashboard pages
- Pandas for loading CSV data into a DataFrame, filtering records, and summarizing columns
- NumPy for numerical calculations on marks arrays
- HTML and CSS for the user interface
- CSV for persistent sample data storage

## 4. Dataset Description

The included `students.csv` file contains 20 illustrative student records. Fields include student ID, name, department, marks in Python, Mathematics and Database, and attendance percentage. Each subject and attendance value is represented on a 0–100 scale. The sample data is fictional and should not be represented as official institutional data.

**Rules used**

- **Pass:** a student must score at least 40 in each subject and have an overall average of at least 50.
- **Grades (based on average marks):** A+ (90–100), A (80–89.99), B (70–79.99), C (60–69.99), D (50–59.99), F (below 50).
- **Attendance:** below 75% is flagged as low. Attendance does not change the marks-based pass/fail result.

## 5. Implementation

1. **Load and validate data:** `load_students()` reads the CSV using Pandas and checks required columns, unique IDs, missing values, numeric values, and mark/attendance ranges.
2. **Calculate marks:** `analyze_students()` converts the subject columns to a NumPy array and calculates total and average marks.
3. **Assign grades:** `assign_grade()` uses conditional statements to apply the grade boundaries listed in the rules above.
4. **Determine result:** a student passes only when each of the three subject marks is at least 40 and the average is at least 50. Attendance is separately flagged as low when below 75%.
5. **Summarize performance:** `get_summary()` calculates class-level metrics, subject averages, grade counts, and the top five students.
6. **Display results:** Flask routes send the processed data to HTML templates. The pages show summary cards, bar charts made with CSS, a searchable/filterable student table, and individual student details.
7. **Export results:** the download route returns the analyzed records as a CSV file.

## 6. Key Features

- Student dataset loaded using Pandas
- NumPy-based total and average calculations
- Reusable functions and conditional logic
- Grades and pass/fail outcomes
- Highest, lowest and class average performance
- Subject-wise average comparison
- Top-five student ranking
- Low-attendance indicator
- Search, department/result filters, and CSV export
- Flask dashboard and individual student pages

## 7. Output and Screenshots

**Dashboard overview and summary cards**

![Dashboard](screenshots/dashboard.png)

**Student directory with filters**

![Student directory](screenshots/students.png)

**Individual student details**

![Student detail](screenshots/student_detail.png)

## 8. Final Outcome

The application turns raw student marks and attendance records into a readable dashboard. It provides an overview of class performance and lets a user inspect individual results, compare subjects, identify top performers, and export analyzed data.

## 9. Challenges and Learning

**1. Search crashed on special characters.**
While testing the student search, typing a character such as `(` caused a server error. The cause was that Pandas `str.contains()` treats the search text as a regular expression by default, so an incomplete pattern failed. I fixed it by adding `regex=False`, so the text is matched literally. I also added automated tests that search for `(`, `[`, `*` and `a.b` to make sure the page no longer crashes.

**2. A student could pass with grade F.**
The original rule only required 40 marks in each subject. One student had 43, 55 and 48 in the three subjects, an average of 48.67 and grade F, but was still marked Pass. This was inconsistent, so I changed the rule: a student passes only with at least 40 in every subject and an average of at least 50. I added unit tests for the boundary cases (an average of 48.33 must fail, and exactly 40 in one subject with an average of exactly 50 must pass), plus a test confirming that no student has both Pass and grade F. After this change the pass rate went from 90% to 85%.

**3. A small coding mistake silently disabled the search filter.**
When I edited the search code, I accidentally left out `students =` before the filter expression. The code ran without any error, but the search stopped filtering because the result was never saved. I noticed this by testing the search with a name and checking the results. This showed me that testing a feature by actually using it matters. I then added a route test that checks searching for "Aarav" shows only Aarav Singh.

**4. Duplicate virtual environments and project cleanliness.**
My project ended up with two virtual environment folders, `.venv` and `.venv-1`. I checked which one the terminal and VS Code were using, kept `.venv`, and deleted the other. I also learned to add a `.gitignore` file so that virtual environments and cache files are not uploaded to GitHub, since `requirements.txt` is enough for someone else to rebuild the environment.

**What I learned**

- How to load and validate CSV data with Pandas, and how to use NumPy for total and average calculations.
- How to keep calculation logic in `analytics.py`, separate from the Flask routes in `app.py`, which made it easy to test.
- How to connect Flask routes to HTML templates and filter records from form input.
- How to write unit tests for boundary conditions and use Flask's test client to test routes.
- How to use Git and GitHub to publish a project while keeping unnecessary files out of the repository.

## 10. GitHub Repository

Repository URL: https://github.com/awanish084/student-performance-analytics