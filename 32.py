from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    profile = {
        "name": "John Doe",
        "title": "Python & Flask Developer",
        "about": "I am a passionate web developer specializing in Python, Flask, and modern web technologies.",
        "skills": ["Python", "Flask", "HTML", "CSS", "JavaScript", "SQL"],
        "projects": [
            "Expense Tracker",
            "Recipe Book App",
            "Blog Website",
            "Portfolio Website"
        ]
    }

    return render_template("index.html", profile=profile)

if __name__ == "__main__":
    app.run(debug=True)