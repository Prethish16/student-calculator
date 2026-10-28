from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    marks1 = ""
    marks2 = ""
    marks3 = ""
    if request.method == "POST":
        try:
            m1 = float(request.form.get("marks1", 0))
            m2 = float(request.form.get("marks2", 0))
            m3 = float(request.form.get("marks3", 0))
            if m1 < 0 or m2 < 0 or m3 < 0 or m1 > 100 or m2 > 100 or m3 > 100:
                result = {"error": "Marks must be between 0 and 100"}
            else:
                total = m1 + m2 + m3
                average = total / 3
                result = {
                    "total": round(total, 2),
                    "average": round(average, 2),
                    "grade": None
                }
            marks1 = request.form.get("marks1", "")
            marks2 = request.form.get("marks2", "")
            marks3 = request.form.get("marks3", "")
        except ValueError:
            result = {"error": "Invalid input. Please enter valid numbers."}
    return render_template("index.html", result=result, marks1=marks1, marks2=marks2, marks3=marks3)
