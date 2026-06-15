from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<title>Internship Management Portal</title>
<style>
body{
    margin:0;
    font-family:Arial,sans-serif;
    background:linear-gradient(135deg,#4facfe,#00f2fe);
}
.navbar{
    background:#222;
    color:white;
    padding:15px;
    text-align:center;
    font-size:24px;
    font-weight:bold;
}
.container{
    width:80%;
    margin:40px auto;
    text-align:center;
}
.card{
    background:white;
    display:inline-block;
    width:300px;
    margin:20px;
    padding:25px;
    border-radius:15px;
    box-shadow:0 5px 15px rgba(0,0,0,0.2);
    transition:0.3s;
}
.card:hover{
    transform:translateY(-10px);
}
.btn{
    display:inline-block;
    background:#4facfe;
    color:white;
    padding:10px 20px;
    text-decoration:none;
    border-radius:5px;
}
.footer{
    text-align:center;
    color:white;
    margin-top:50px;
}
</style>
</head>
<body>

<div class="navbar">
🎓 Internship Management Portal
</div>

<div class="container">
    <h1 style="color:white;">Find Your Dream Internship</h1>

    <div class="card">
        <h2>👨‍🎓 Student Panel</h2>
        <p>Browse internships, apply online, and track your application status.</p>
        <a class="btn" href="/student">Open</a>
    </div>

    <div class="card">
        <h2>🏢 Company Panel</h2>
        <p>Post internships, manage applicants, and hire talented students.</p>
        <a class="btn" href="/company">Open</a>
    </div>

    <div class="card">
        <h2>⚙️ Admin Panel</h2>
        <p>Manage students, companies, internships, and applications.</p>
        <a class="btn" href="/admin">Open</a>
    </div>
</div>

<div class="footer">
    <h3>© 2026 Internship Management Portal</h3>
</div>

</body>
</html>
"""

@app.route("/student")
def student():
    return """
    <h1>👨‍🎓 Student Dashboard</h1>
    <p>Apply for internships and track applications.</p>
    <a href="/">Back</a>
    """

@app.route("/company")
def company():
    return """
    <h1>🏢 Company Dashboard</h1>
    <p>Post internships and manage applicants.</p>
    <a href="/">Back</a>
    """

@app.route("/admin")
def admin():
    return """
    <h1>⚙️ Admin Dashboard</h1>
    <p>Manage portal data and users.</p>
    <a href="/">Back</a>
    """

if __name__ == "__main__":
    app.run(debug=True)