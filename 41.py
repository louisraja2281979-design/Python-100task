from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    videos = os.listdir(app.config["UPLOAD_FOLDER"])
    return render_template("index.html", videos=videos)

@app.route("/upload", methods=["POST"])
def upload_video():
    if "video" not in request.files:
        return redirect(url_for("index"))

    file = request.files["video"]

    if file.filename == "":
        return redirect(url_for("index"))

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(filepath)

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)