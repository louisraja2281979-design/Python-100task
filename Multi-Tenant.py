from flask import Flask, render_template_string, request, redirect, session

app = Flask(__name__)
app.secret_key = "admin123"

# Sample tenants
tenants = {
    "Company A": {"users": 25},
    "Company B": {"users": 15},
    "Company C": {"users": 40}
}

LOGIN_PAGE = """
<!DOCTYPE html>
<html>
<head>
<title>Multi-Tenant Dashboard</title>
<style>
body{font-family:Arial;background:#f4f4f4;text-align:center;padding:50px;}
.box{background:white;padding:20px;width:300px;margin:auto;border-radius:10px;}
input{width:90%;padding:10px;margin:10px;}
button{padding:10px 20px;background:#007bff;color:white;border:none;}
</style>
</head>
<body>
<div class="box">
<h2>Admin Login</h2>
<form method="post">
<input type="text" name="username" placeholder="Username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Login</button>
</form>
</div>
</body>
</html>
"""

DASHBOARD = """
<!DOCTYPE html>
<html>
<head>
<title>Dashboard</title>
<style>
body{font-family:Arial;background:#eef2f7;padding:20px;}
.card{
background:white;
padding:15px;
margin:10px;
border-radius:10px;
box-shadow:0 0 10px #ccc;
}
a{color:red;text-decoration:none;}
</style>
</head>
<body>
<h1>Multi-Tenant Admin Dashboard</h1>
<p><a href="/logout">Logout</a></p>

{% for name,data in tenants.items() %}
<div class="card">
<h3>{{name}}</h3>
<p>Users: {{data['users']}}</p>
</div>
{% endfor %}

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["username"] == "admin" and request.form["password"] == "admin":
            session["logged_in"] = True
            return redirect("/dashboard")
    return render_template_string(LOGIN_PAGE)

@app.route("/dashboard")
def dashboard():
    if not session.get("logged_in"):
        return redirect("/")
    return render_template_string(DASHBOARD, tenants=tenants)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)