from flask import Flask, render_template_string, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"

# Create database
conn = sqlite3.connect("blog.db")
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS posts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    content TEXT
)
""")
conn.commit()
conn.close()

HOME = """
<h1>My Blog</h1>

{% for post in posts %}
<h2>{{ post[1] }}</h2>
<p>{{ post[2] }}</p>
<hr>
{% endfor %}

<a href="/login">Admin Login</a>
"""

LOGIN = """
<h2>Admin Login</h2>

<form method="post">
Username:<br>
<input type="text" name="username"><br><br>

Password:<br>
<input type="password" name="password"><br><br>

<button type="submit">Login</button>
</form>
"""

ADMIN = """
<h1>Admin Panel</h1>

<a href="/add">Add Post</a> |
<a href="/logout">Logout</a>

<hr>

{% for post in posts %}
<h3>{{ post[1] }}</h3>

<a href="/edit/{{ post[0] }}">Edit</a>
<a href="/delete/{{ post[0] }}">Delete</a>

<hr>
{% endfor %}
"""

ADD = """
<h2>Add Blog Post</h2>

<form method="post">
Title:<br>
<input type="text" name="title"><br><br>

Content:<br>
<textarea name="content" rows="10" cols="50"></textarea><br><br>

<button type="submit">Publish</button>
</form>
"""

EDIT = """
<h2>Edit Post</h2>

<form method="post">
Title:<br>
<input type="text" name="title" value="{{ post[1] }}"><br><br>

Content:<br>
<textarea name="content" rows="10" cols="50">{{ post[2] }}</textarea><br><br>

<button type="submit">Update</button>
</form>
"""

@app.route("/")
def home():
    conn = sqlite3.connect("blog.db")
    posts = conn.execute("SELECT * FROM posts").fetchall()
    conn.close()
    return render_template_string(HOME, posts=posts)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["username"] == "admin" and request.form["password"] == "admin123":
            session["admin"] = True
            return redirect("/admin")
    return render_template_string(LOGIN)

@app.route("/admin")
def admin():
    if "admin" not in session:
        return redirect("/login")

    conn = sqlite3.connect("blog.db")
    posts = conn.execute("SELECT * FROM posts").fetchall()
    conn.close()

    return render_template_string(ADMIN, posts=posts)

@app.route("/add", methods=["GET", "POST"])
def add():
    if "admin" not in session:
        return redirect("/login")

    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]

        conn = sqlite3.connect("blog.db")
        conn.execute(
            "INSERT INTO posts(title, content) VALUES(?, ?)",
            (title, content)
        )
        conn.commit()
        conn.close()

        return redirect("/admin")

    return render_template_string(ADD)

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    if "admin" not in session:
        return redirect("/login")

    conn = sqlite3.connect("blog.db")

    if request.method == "POST":
        conn.execute(
            "UPDATE posts SET title=?, content=? WHERE id=?",
            (request.form["title"],
             request.form["content"],
             id)
        )
        conn.commit()
        conn.close()

        return redirect("/admin")

    post = conn.execute(
        "SELECT * FROM posts WHERE id=?",
        (id,)
    ).fetchone()

    conn.close()

    return render_template_string(EDIT, post=post)

@app.route("/delete/<int:id>")
def delete(id):
    if "admin" not in session:
        return redirect("/login")

    conn = sqlite3.connect("blog.db")
    conn.execute("DELETE FROM posts WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return redirect("/admin")

@app.route("/logout")
def logout():
    session.pop("admin", None)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)