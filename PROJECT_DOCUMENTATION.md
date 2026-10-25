# Project Documentation: Student Performance Analytics System

## 1. Project Title and Student Details

**Project:** Student Performance Analytics System  
**Student Name:** AWANISH SHARMA  
**Course:** EWB Courses — Python with AI  
**Institution:** VEER BAHADUR SINGH PURVANCHAL UNIVERSITY JAUNPUR ,UTTAR PRADESH  
**Submission Date:** 26 October 2026  
**GitHub Repository:** [Paste your repository URL here]

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

## 5. Implementation

1. **Load and validate data:** `load_students()` reads the CSV using Pandas and checks required columns, unique IDs, missing values, numeric values, and mark/attendance ranges.
2. **Calculate marks:** `analyze_students()` converts the subject columns to a NumPy array and calculates total and average marks.
3. **Assign grades:** `assign_grade()` uses conditional statements to apply the grade boundaries listed in this document.
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

After running the application, capture screenshots of:
- Dashboard overview and summary cards
- Subject performance and grade distribution
- Top performers table
- Student directory with filters
- Individual student details

Insert the screenshots here before final submission.

## 8. Final Outcome

The application turns raw student marks and attendance records into a readable dashboard. It provides an overview of class performance and lets a user inspect individual results, compare subjects, identify top performers, and export analyzed data.

## 9. Challenges and Learning

Complete this section after testing the project. Describe actual issues you encountered and how you solved them. Suggested topics to reflect on include validating CSV data, keeping calculations reusable, connecting Flask routes to templates, filtering student records, and testing boundary conditions for grades and pass/fail logic. Do not claim a challenge unless you actually encountered it.

## 10. GitHub Repository

Repository URL: [Paste the final public repository URL here]

Before submitting, verify that the repository contains the Python files, CSV dataset, templates, stylesheet, tests, README, and this documentation. Submit the repository URL through the Google Form provided by the course trainer and save the submission confirmation.
