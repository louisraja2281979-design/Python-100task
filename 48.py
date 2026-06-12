from flask import Flask, render_template, request
import cv2
import os
import uuid

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
RESULT_FOLDER = "static/results"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

face_cascade = cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml"
)

@app.route("/", methods=["GET", "POST"])
def index():
    result_image = None
    face_count = 0

    if request.method == "POST":
        file = request.files["image"]

        if file:
            filename = str(uuid.uuid4()) + ".jpg"
            upload_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(upload_path)

            img = cv2.imread(upload_path)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30)
            )

            face_count = len(faces)

            for (x, y, w, h) in faces:
                cv2.rectangle(
                    img,
                    (x, y),
                    (x + w, y + h),
                    (0, 255, 0),
                    2
                )

            result_filename = "result_" + filename
            result_path = os.path.join(
                RESULT_FOLDER,
                result_filename
            )

            cv2.imwrite(result_path, img)

            result_image = result_filename

    return render_template(
        "index.html",
        result_image=result_image,
        face_count=face_count
    )

if __name__ == "__main__":
    app.run(debug=True)