from flask import Flask, render_template, request

app = Flask(__name__)

students = {
    "pavani": {
        "password": "1234",
        "marks": {
            "Maths": 80,
            "Science": 25,
            "English": 60
        }
    }
}

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/marks', methods=['POST'])
def marks():

    username = request.form['username']
    password = request.form['password']

    if username in students and students[username]["password"] == password:

        student_marks = students[username]["marks"]

        results = {}

        for subject, mark in student_marks.items():

            if mark >= 30:
                results[subject] = (mark, "Pass")
            else:
                results[subject] = (mark, "Fail")

        return render_template("marks.html",
                               username=username,
                               results=results)

    return "Invalid Username or Password"

if __name__ == '__main__':
    app.run(debug=True)