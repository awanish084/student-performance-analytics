from flask import Flask, abort, make_response, render_template, request
from analytics import SUBJECT_COLUMNS, analyze_students, get_summary, load_students

app = Flask(__name__)


def get_analyzed_data():
    return analyze_students(load_students())


@app.route("/")
def dashboard():
    students = get_analyzed_data()
    summary = get_summary(students)
    subject_rows = [
        {"name": subject.title(), "average": average}
        for subject, average in summary["subject_averages"].items()
    ]
    grade_rows = [
        {"grade": grade, "count": count}
        for grade, count in summary["grade_counts"].items()
    ]
    return render_template(
        "index.html",
        summary=summary,
        subject_rows=subject_rows,
        grade_rows=grade_rows,
    )


@app.route("/students")
def student_list():
    students = get_analyzed_data()
    query = request.args.get("q", "").strip()
    result_filter = request.args.get("result", "").strip()
    department_filter = request.args.get("department", "").strip()

    if query:
        students = students[
            students["name"].str.contains(query, case=False, na=False, regex=False)
            | students["student_id"].astype(str).str.contains(query, case=False, na=False, regex=False)
        ] 
    if result_filter in {"Pass", "Fail"}:
        students = students[students["result"] == result_filter]
    if department_filter:
        students = students[students["department"] == department_filter]

    departments = sorted(load_students()["department"].dropna().unique().tolist())
    records = students.sort_values(["average", "name"], ascending=[False, True]).to_dict(orient="records")
    return render_template(
        "students.html",
        students=records,
        query=query,
        result_filter=result_filter,
        department_filter=department_filter,
        departments=departments,
    )


@app.route("/students/<student_id>")
def student_detail(student_id):
    students = get_analyzed_data()
    match = students[students["student_id"].astype(str) == str(student_id)]
    if match.empty:
        abort(404)
    student = match.iloc[0].to_dict()
    subjects = [{"name": subject.title(), "marks": int(student[subject])} for subject in SUBJECT_COLUMNS]
    return render_template("student_detail.html", student=student, subjects=subjects)


@app.route("/download")
def download_csv():
    students = get_analyzed_data()
    csv_text = students.to_csv(index=False)
    response = make_response(csv_text)
    response.headers["Content-Disposition"] = "attachment; filename=student_analysis.csv"
    response.headers["Content-Type"] = "text/csv; charset=utf-8"
    return response


@app.errorhandler(404)
def not_found(_error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
