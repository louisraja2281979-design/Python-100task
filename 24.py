from flask import Flask, render_template_string, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create uploads folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>File Upload System</title>
</head>
<body>
    <h2>Upload a File</h2>

    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="file" required>
        <button type="submit">Upload</button>
    </form>

    {% if message %}
        <p>{{ message }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def upload_file():
    message = ""

    if request.method == "POST":
        if "file" not in request.files:
            message = "No file selected"
        else:
            file = request.files["file"]

            if file.filename == "":
                message = "No file selected"
            else:
                filepath = os.path.join(
                    app.config["UPLOAD_FOLDER"],
                    file.filename
                )
                file.save(filepath)
                message = f"File uploaded successfully: {file.filename}"

    return render_template_string(HTML, message=message)

if __name__ == "__main__":
    app.run(debug=True)